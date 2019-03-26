from settings.core import *


INSTALLED_APPS = [
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "djangocms_text_ckeditor",
    "django.contrib.sitemaps",
    "theme",
    "access_control",
    "stock",
    "cms",
    "menus",
    "treebeard",
    "filer",
    "easy_thumbnails",
    "mptt",
    "djangocms_link",
    "djangocms_file",
    "djangocms_picture",
    "djangocms_video",
    "djangocms_googlemap",
    "djangocms_snippet",
    "djangocms_style",
    "djangocms_column",
    # ThirdParty
    "sass_processor",
    "sekizai",
    # "sorl.thumbnail",
    "rest_framework",
    "webpack_loader",
    "rest_framework.authtoken",
    "hvad",
]

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

THUMBNAIL_ALIASES = {
    '': {
        'default': {'size': (341, 227), 'crop': True},
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    # 'cms.middleware.utils.ApphookReloadMiddleware'
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = "inventory.urls"

SASS_PRECISION = 8

SASS_PROCESSOR_ROOT = STATIC_ROOT

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

STATICFILES_DIRS = [
    # ('node_modules', '/node_modules/'),
]
#
STATIC_URL = "/static/"

SITE_ID = 1

NODE_MODULES_URL = STATIC_URL + "node_modules/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
            ]
        },
    }
]

CMS_TEMPLATES = [
    ("theme/pages/portal.html", "HomePage template"),
    ("theme/pages/content.html", "Content template"),
]

WSGI_APPLICATION = "inventory.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


LANGUAGES = [("en", "English"), ("nl", "Nederlands")]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_TO_REDIRECT_URL = "theme:default"

LOGOUT_TO_REDIRECT_URL = "theme:default"

PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.SHA1PasswordHasher",
    "django.contrib.auth.hashers.MD5PasswordHasher",
    "django.contrib.auth.hashers.CryptPasswordHasher",
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "nl"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"


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
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}


