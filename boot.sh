#!/bin/sh

source venv/bin/activate
# flask db upgrade
# flask translate compile

# Utilisation gunicorn pour lancer le serveur
exec gunicorn -b :80 --access-logfile - --error-logfile - "VahenWeb:create_server()"