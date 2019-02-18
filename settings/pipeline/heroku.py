from settings.pipeline.prod import *

ALLOWED_HOSTS = ['*']

DEBUG = True

sentry_sdk.init(
    dsn="https://619102194c75442c9dd288ee8efe7144@sentry.io/1393371",
    integrations=[DjangoIntegration()]
)
