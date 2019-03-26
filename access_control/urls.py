from django.urls import path, register_converter, re_path

from access_control import views, converters

app_name = "access_control"

urlpatterns = [
    path("create/", views.UserCreate.as_view(), name="user_create"),
    path("login/", views.LoginView.as_view(), name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    re_path(
        r"^activate/(?P<uuid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        views.activate,
        name="activate",
    ),
]
