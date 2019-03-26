from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from stock.models.items.assets import audio_visual


class AudioVisualKindSerializer(serializers.ModelSerializer):
    # audio_visuals = serializers.StringRelatedField(many=True)

    class Meta:
        model = audio_visual.Kind
        fields = "__all__"


class AudioVisualBrandSerializer(CountryFieldMixin, serializers.ModelSerializer):
    # audio_visuals = serializers.StringRelatedField(many=True)

    class Meta:
        model = audio_visual.Brand
        fields = "__all__"


class AudioVisualSerializer(serializers.ModelSerializer):
    # kind = AudioVisualKindSerializer(many=True, read_only=True)
    # brand = AudioVisualBrandSerializer(many=True, read_only=True)

    class Meta:
        model = audio_visual.AudioVisual
        fields = "__all__"


class ScreenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_visual.ScreenType
        fields = '__all__'


class MountingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_visual.ScreenMountingMethod
        fields = '__all__'
