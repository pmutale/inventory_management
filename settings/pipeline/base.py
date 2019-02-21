from settings.core import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'theme',
    'access_control',
    'stock',

    #ThirdParty
    'sass_processor',
    'sekizai',
    'sorl.thumbnail',
    'rest_framework',
    'webpack_loader',
    'rest_framework.authtoken',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inventory.urls'

SASS_PRECISION = 8

SASS_PROCESSOR_ROOT = STATIC_ROOT

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

STATICFILES_DIRS = [
    # ('node_modules', '/node_modules/'),
]
#
STATIC_URL = '/static/'

NODE_MODULES_URL = STATIC_URL + 'node_modules/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'inventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_TO_REDIRECT_URL = 'theme:default'

LOGOUT_TO_REDIRECT_URL = 'theme:default'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'nl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


def read_pgpass(dbname, host=None, port=None, engine=None, env=None):
    """
    Intends to read the .pgpass file stored on the local environment. Its the intentions
    that everyone make that file on their dev environment
    ==> http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
    :param engine:
    :param port:
    :param host:
    :param dbname: Database name
    :return:
    """
    import sys
    from pathlib import Path

    home_path = str(Path.home())

    no_database_found = """
        Your {path}/.pgpass file doesn"t have database "{dbname}" for host "{host}:{port}".

        To switch to a PostgreSQL database, add a line to the ~/.pgpass file
        containing it"s credentials.
        See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
        """.format(
        dbname=dbname, path=home_path, host=host or "*", port=port or "*"
    )
    no_pgpass_notification = """
    You don"t have a {0}/.pgpass file so. Please create one!

    To switch to a PostgreSQL database, create a ~/.pgpass file
    containing it"s credentials.
    See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
    """.format(
        home_path
    )

    try:
        pgpass = os.path.join(home_path, ".pgpass")
        pgpass_lines = open(pgpass).read().split()
    except IOError:
        # Print instructions
        print(no_pgpass_notification)
    else:
        for match in (dbname, "*"):
            for line in pgpass_lines:
                words = line.strip().split(":")
                if (
                        words[2] == match
                        and words[0] == (host or words[0])
                        and words[1] == (port or words[1])
                ):
                    return dict(
                        ENGINE=engine,
                        NAME=dbname,
                        USER=words[3],
                        PASSWORD=words[4],
                        HOST=words[0],
                        PORT=words[1],
                    )
        print(no_database_found)
    return sys.exit(
        "Error: You don't have a database setup, Please create a ~/.pgpass file "
    )


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(asctime)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024 * 2,
            "backupCount": 15,
            "filename": os.path.join(BASE_DIR, "var", "log", "mysite.log"),
            "formatter": "verbose",
        },
        "dbfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024 * 2,
            "backupCount": 15,
            "filename": os.path.join(BASE_DIR, "var", "log", "db.log"),
            "formatter": "simple",
        },
        "timerfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024 * 2,
            "backupCount": 15,
            "filename": os.path.join(BASE_DIR, "var", "log", "timer.log"),
            "formatter": "simple",
        },
    },
    "loggers": {
        "django.request": {"handlers": ["file"], "level": "INFO", "propagate": True},
        "django.db.backends": {
            "handlers": ["dbfile"],
            "level": "INFO",
            "propagate": True,
        },
        "requesttimer": {"level": "INFO", "propagate": True, "handlers": ["timerfile"]},
        "": {"handlers": ["file"], "level": "DEBUG", "propagate": True},
        "inventory": {"handlers": ["file"], "level": "DEBUG", "propagate": True},
    },
}

LOG_LEVELS = (
    ("INFO", "Info"),
    ("WARNING", "Warning"),
    ("ERROR", "Error"),
    ("EXCEPTION", "Exception"),
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

