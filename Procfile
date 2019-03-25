web: gunicorn inventory.wsgi --log-file -
release: python manage.py start_site && python manage.py compilescss --use-processor-root && python manage.py collectstatic --no-input --ignore=*.scss
