from settings.pipeline.prod import *
from sentry_sdk.integrations.django import DjangoIntegration


ALLOWED_HOSTS = ["*"]

DEBUG = False

STATIC_ROOT = "staticfiles"

sentry_sdk.init(
    dsn="https://619102194c75442c9dd288ee8efe7144@sentry.io/1393371",
    integrations=[DjangoIntegration()],
)
