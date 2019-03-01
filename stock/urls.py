from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stock import views

urlpatterns = [
    path("audio_visual/", views.AudioVisualList.as_view()),
    path("audio_visual/<int:pk>/", views.AudioVisualDetail.as_view()),
    path("audio_visual/brand/<int:pk>/", views.AudioVisualBrandDetail.as_view()),
    path("audio_visual/brand/", views.AudioVisualBrandList.as_view()),
    path("audio_visual/kind/<int:pk>/", views.AudioVisualKindDetail.as_view()),
    path("audio_visual/kind/", views.AudioVisualKindList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
