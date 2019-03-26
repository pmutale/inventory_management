from settings.pipeline.prod import *

from settings.helpers import read_pgpass

ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
    "default": read_pgpass(
        "inventory",
        env="dev",
        host="localhost",
        engine="django.db.backends.postgresql_psycopg2",
    )
}
