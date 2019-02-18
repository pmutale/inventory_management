from django.urls import path

from theme import views

urlpatterns = [
    path('', views.default, name='default')
]
