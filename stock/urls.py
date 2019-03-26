from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stock import views

app_name = "stock"

urlpatterns = [
    path("audio_visual/", views.AudioVisualList.as_view(), name="audio_visual"),
    path(
        "audio_visual/<int:pk>/",
        views.AudioVisualDetail.as_view(),
        name="detail_audio_visual",
    ),
    path(
        "audio_visual/brand/<int:pk>/",
        views.AudioVisualBrandDetail.as_view(),
        name="av_brand",
    ),
    path(
        "audio_visual/brand/",
        views.AudioVisualBrandList.as_view(),
        name="list_av_brand",
    ),
    path(
        "audio_visual/kind/<int:pk>/",
        views.AudioVisualKindDetail.as_view(),
        name="av_kind",
    ),
    path(
        "audio_visual/kind/", views.AudioVisualKindList.as_view(), name="list_av_kind"
    ),
    path(
        "audio_visual/screen_type/",
        views.AudioVisualKindScreenTypeList.as_view(),
        name="list_av_kind_screen_type",
    ),
    path(
        "audio_visual/screen_type/<int:pk>",
        views.AudioVisualKindScreenTypeDetail.as_view(),
        name="detail_av_kind_screen_type",
    ),
    path(
        "audio_visual/mounting_method/",
        views.AudioVisualKindMountingList.as_view(),
        name="list_av_kind_mounting_method",
    ),
    path(
        "audio_visual/mounting_method/<int:pk>",
        views.AudioVisualKindMountingDetail.as_view(),
        name="detail_av_kind_mounting_method",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
