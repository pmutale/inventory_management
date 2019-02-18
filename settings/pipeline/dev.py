from settings.pipeline.base import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

DATABASES = {
    'default':
        read_pgpass(
            'inventory',
            env='dev',
            host='localhost',
            engine='django.db.backends.postgresql_psycopg2')
}
