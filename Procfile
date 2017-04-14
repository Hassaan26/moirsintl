web: gunicorn --preload --log-file=- moirs.wsgi:application
web: python moirsintl/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT moirs/settings.py