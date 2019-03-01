from settings.pipeline.base import *

import django_heroku

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-prod.json"),
    }
}

django_heroku.settings(locals())
