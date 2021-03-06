from cms.utils import get_current_site
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext as _

from access_control.models import Employee
from access_control.validators import ValidatePasswordStrength


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "validators": [ValidatePasswordStrength("password")],
            }
        }

    def create(self, validated_data):
        context = {"username": None, "success": False, "error": False}
        try:
            user = User(
                email=validated_data["email"],
                username=validated_data["username"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
            )
            user.set_password(validated_data["password"])
            user.is_active = False
            user.save()

            Employee.objects.create(user=user)
            Token.objects.create(user=user)

            #  # TODO Email activation in production
            # current_site = get_current_site()
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            #     'token': Token.objects.filter(user=user).values_list('key', flat=True),
            # })
            # to_email = validated_data['email']
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            # email.send()
            # #

            setattr(
                JsonResponse,
                "username",
                _(
                    f"User with username, {user.username} has been successfully created."
                ),
            )
            return JsonResponse
        except Exception as e:
            context["error"] = str(e)
            return JsonResponse(context, json_dumps_params={"indent": 4})
