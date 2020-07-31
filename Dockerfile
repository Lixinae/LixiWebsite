FROM python:3.8-alpine

RUN adduser -D VahenWebsite

WORKDIR /home/VahenWebsite

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy le fichier dans le file system de l'image
COPY requirements.txt requirements.txt

RUN python -m venv venv

RUN venv/bin/pip install --upgrade pip
# Install les requirements du projet
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

# Copy des dossiers de l'applications
COPY application application

# Copy des scripts de migration de DB
# COPY migrations migrations

# Copy des scripts a la racine de l'image
COPY VahenWeb.py boot.sh loggingConfig.yaml ./

# Ajout du droit d'execution sur le fichier de boot
RUN chmod +x boot.sh

# Fixe la variable d'environnement
ENV FLASK_APP VahenWeb.py

RUN chown -R VahenWebsite:VahenWebsite ./
#USER Vahen

# Ouverture du port 80
EXPOSE 80

# execution du script boot.sh
ENTRYPOINT ["./boot.sh"]
