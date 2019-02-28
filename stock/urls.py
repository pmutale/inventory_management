from django.urls import path

from stock.views import Inventories

urlpatterns = [path("", Inventories.as_view(), name="inventory")]
