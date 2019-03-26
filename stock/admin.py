from django.contrib import admin
from hvad.admin import TranslatableAdmin

from stock import models
from stock.models.items.assets import audio_visual
from stock.models.items.assets.computer import Peripheral


admin.site.register(models.Category)
admin.site.register(audio_visual.AudioVisual)
admin.site.register(audio_visual.Kind)
admin.site.register(audio_visual.Brand)
admin.site.register(audio_visual.ScreenType)
admin.site.register(audio_visual.ScreenMountingMethod)
admin.site.register(Peripheral)
