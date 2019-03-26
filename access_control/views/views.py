from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics

from access_control.helpers import account_activation_token
from access_control.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(settings.LOGOUT_TO_REDIRECT_URL))


def activate(request, uuid, token):
    try:
        uid = force_text(urlsafe_base64_decode(uuid))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.employee.email_confirmed = True
        user.save()
        user.employee.save()
        login(request, user)
        return redirect("theme:default")
    else:
        return HttpResponse("Activation link is invalid!")
