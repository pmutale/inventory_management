web: gunicorn inventory.wsgi --log-file -
release: python manage.py migrate
release: python manage.py compilescss --use-processor-root
release: python manage.py collectstatic --no-input
