import os

if os.environ.get("IS_HEROKU_DEV", None):
    from settings.pipeline.heroku import *
elif os.environ.get("IS_HEROKU_PRD", None):
    from settings.pipeline.prod import *
elif os.environ.get("IS_GITBUCKET", None):
    from settings.pipeline.bitbucket import *
else:
    from settings.pipeline.dev import *
