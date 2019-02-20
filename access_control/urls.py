from django.urls import path

from access_control.views import LoginView, UserCreate, user_logout

app_name = 'access_control'

urlpatterns = [
    path("create/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="user_login"),
    path("logout/", user_logout, name="user_logout")

]
