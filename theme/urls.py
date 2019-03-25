from django.urls import path

from theme import views


app_name = "theme"

urlpatterns = [path("", views.default, name="default")]
