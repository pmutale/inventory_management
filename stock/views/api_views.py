from rest_framework import generics

from stock.models.items.assets import audio_visual
from stock import serializers


class AudioVisualList(generics.ListCreateAPIView):
    queryset = audio_visual.AudioVisual.objects.all()
    serializer_class = serializers.AudioVisualSerializer


class AudioVisualDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = audio_visual.AudioVisual.objects.all()
    serializer_class = serializers.AudioVisualSerializer


class AudioVisualKindList(generics.ListCreateAPIView):
    queryset = audio_visual.Kind.objects.all()
    serializer_class = serializers.AudioVisualKindSerializer


class AudioVisualKindDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = audio_visual.Kind.objects.all()
    serializer_class = serializers.AudioVisualKindSerializer


class AudioVisualBrandList(generics.ListCreateAPIView):
    queryset = audio_visual.Brand.objects.all()
    serializer_class = serializers.AudioVisualBrandSerializer


class AudioVisualBrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = audio_visual.Brand.objects.all()
    serializer_class = serializers.AudioVisualBrandSerializer
