web: gunicorn inventory.wsgi --log-file -
release: python manage.py migrate && python manage.py compilescss --use-processor-root && python manage.py collectstatic --no-input
