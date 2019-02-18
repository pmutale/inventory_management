web: gunicorn inventory.wsgi --log-file -
web: node npm run build-production
release: python manage.py migrate
