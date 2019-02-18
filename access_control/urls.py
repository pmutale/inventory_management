from django.urls import path

from access_control.views import LoginView, UserCreate

urlpatterns = [
    path("create/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="user_login")
]
