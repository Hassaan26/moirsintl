web: python manage.py collectstatic --noinput; gunicorn moirsintl.wsgi  --workers=4 --bind=0.0.0.0:$PORT
