import os
if os.environ.get('IS_HEROKU_DEV', None) or os.environ.get('IS_LOCAL', None):
    from settings.pipeline.dev import *
elif os.environ.get('IS_HEROKU_PRD', None):
    from settings.pipeline.prod import *

