from django.utils.translation import gettext as _


class UserEmailNotConfirmedException(Exception):
    def __init___(self, message):
        message = _("User account not validated/Confirmed")
        self.message = message
