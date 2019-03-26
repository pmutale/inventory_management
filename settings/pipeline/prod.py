from settings.pipeline.base import *

import django_heroku

DEBUG = False

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-prod.json"),
    }
}

django_heroku.settings(locals())

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "p.mutale@developers.nl"
EMAIL_HOST_PASSWORD = "cnggiwselgiccmip"
