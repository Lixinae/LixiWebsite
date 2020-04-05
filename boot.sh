#!/bin/sh

source venv/bin/activate
# flask db upgrade
# flask translate compile

# Utilisation gunicorn pour lancer le serveur
# Todo -> Remettre plus tard
exec gunicorn -b :5000 --access-logfile - --error-logfile - "VahenWeb:create_server()"