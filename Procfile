web: gunicorn inventory.wsgi --log-file -
web: npm run build-production
release: python manage.py migrate
