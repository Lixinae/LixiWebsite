FROM python:3.7-alpine

RUN adduser -D VahenWebsite

WORKDIR /home/VahenWebsite

# Copy le fichier dans le file system de l'image
COPY requirements.txt requirements.txt

RUN python -m venv venv

# Install les requirements du projet
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

# Copy des dossiers de l'applications
COPY app app

# Copy des scripts de migration de DB
COPY migrations migrations

# Copy des scripts a la racine de l'image
COPY VahenWebsite.py config.py boot.sh ./

# Ajout du droit d'execution sur le fichier de boot
RUN chmod +x boot.sh

# Fixe la variable d'environnement
ENV FLASK_APP VahenWebsite.py

RUN chown -R VahenWebsite:VahenWebsite ./
USER Vahen

# Ouverture du port 5000
EXPOSE 5000

# execution du script boot.sh
ENTRYPOINT ["./boot.sh"]
