#!/usr/bin/env bash
# exit on error
set -o errexit

# pip install -r requirements.txt
# python manage.py collectstatic --no-input
# python manage.py migrate
echo "Migrando banco de dados..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput