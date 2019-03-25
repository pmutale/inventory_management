from django.utils.translation import ugettext as _
from rest_framework import serializers


class ValidatePasswordStrength:
    def __init__(self, password_field):
        self.password = password_field

    def set_context(self, serializer_field):
        self.serializer_field = serializer_field

    def __call__(self, value):
        password = value

        min_length = 8

        if len(password) < min_length:
            raise serializers.ValidationError(
                _(f"Password must be at least {min_length} characters long.")
            )

        # check for digit
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError(
                _("Password must contain at least 1 digit.")
            )

        # check for letter
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError(
                _("Password must contain at least 1 letter.")
            )
