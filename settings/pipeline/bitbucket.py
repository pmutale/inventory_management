from settings.helpers import read_pgpass
from settings.pipeline.prod import *

DATABASES = {
    "default": read_pgpass(
        "inventory",
        env="dev",
        host="localhost",
        engine="django.db.backends.postgresql_psycopg2",
    )
}
