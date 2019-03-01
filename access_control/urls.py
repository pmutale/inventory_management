from django.urls import path

from access_control import views

app_name = "access_control"

urlpatterns = [
    path("create/", views.UserCreate.as_view(), name="user_create"),
    path("login/", views.LoginView.as_view(), name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path(
        "activate/<uuid:uuid>/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",
        views.activate,
        name="activate",
    ),
]
