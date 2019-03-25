from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from stock.models.items.assets import audio_visual


class AudioVisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_visual.AudioVisual
        fields = "__all__"


class AudioVisualKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_visual.Kind
        fields = "__all__"


class AudioVisualBrandSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = audio_visual.Brand
        fields = "__all__"
