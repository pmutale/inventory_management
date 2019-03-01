from django.contrib import admin
from hvad.admin import TranslatableAdmin

from stock import models
from stock.models.items.assets import audio_visual

from stock.models.items.assets.computer import Image, Peripheral, PeripheralDetails


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


class ComputerAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

    def save_model(self, request, obj, form, change):
        super(ComputerAdmin, self).save_model(request, obj, form, change)

        for afile in request.FILES.getlist("photos_multiple"):
            obj.images.create(file=afile)


admin.site.register(models.Computer, ComputerAdmin)
admin.site.register(models.Category)
admin.site.register(audio_visual.AudioVisual)
admin.site.register(Peripheral)
