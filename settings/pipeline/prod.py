from settings.pipeline.base import *

if os.environ.get('IS_AZURE'):
    DATABASES = {
        'default':
            read_pgpass(
                'inventory',
                host='inventory-app-developers.postgres.database.azure.com',
                engine='django.db.backends.postgresql_psycopg2')
    }
