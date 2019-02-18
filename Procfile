web: gunicorn inventory.wsgi --log-file -
release: python manage.py migrate
release: npm run build-production
release: touch staticfiles/bundles
release: touch webpack-stats-prod.json
