web: gunicorn inventory.wsgi --log-file -
release: python manage.py migrate
release: npm run build &&
npm run build-production
