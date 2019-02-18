from settings.pipeline.base import *

import django_heroku

DEBUG = False

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

django_heroku.settings(locals())
