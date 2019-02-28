from django.contrib import admin
from hvad.admin import TranslatableAdmin

from stock.models import Computer, Category, Inventory, Details
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


# class InventoryAdmin(TranslatableAdmin):
#     list_display = ("get_item_translated",)


admin.site.register(Computer, ComputerAdmin)
# admin.site.register(Category)
# admin.site.register(Details)
# admin.site.register(PeripheralDetails)
admin.site.register(Peripheral)
# admin.site.register(Inventory)
