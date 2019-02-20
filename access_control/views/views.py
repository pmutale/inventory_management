from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics

from access_control.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(settings.LOGOUT_TO_REDIRECT_URL))

