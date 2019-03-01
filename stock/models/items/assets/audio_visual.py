from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from djchoices import DjangoChoices, ChoiceItem

from stock.models import Category, get_upload_path
from stock.models.items.assets.base import ItemBaseModel


class AudioExtra(models.Model):
    is_wireless = models.BooleanField(default=False)


class Brand(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    country_of_origin = CountryField(multiple=True)
    brand_number = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(help_text=_("Help describe this brand"))

    def __str__(self):
        return f"{self.name} - {self.brand_number}"


class Kind(models.Model):
    class MountingMethod(DjangoChoices):
        Wall_or_Ceiling = ChoiceItem(_("wall_ceiling"))
        Tripod = ChoiceItem(_("tripod"))

    class ScreenType(DjangoChoices):
        Folding = ChoiceItem(_("folding"))
        Tripod = ChoiceItem(_("tripod"))
        LCD = ChoiceItem(_("lcd"))
        LED = ChoiceItem(_("led"))
        PLASMA = ChoiceItem(_("plasma"))
        OLED = ChoiceItem(_("oled"))

    name = models.CharField(max_length=128, blank=True, null=True)
    screen_size = models.CharField(max_length=128, blank=True, null=True)
    screen_type = models.CharField(
        max_length=64, choices=ScreenType, blank=True, null=True
    )
    mounting_method = models.CharField(
        max_length=64, choices=MountingMethod, blank=True, null=True
    )
    overall_width = models.CharField(max_length=128, blank=True, null=True)
    overall_height = models.CharField(max_length=128, blank=True, null=True)
    color = models.CharField(max_length=128, blank=True, null=True)
    extras = models.TextField(max_length=128, blank=True, null=True)
    audio = models.ForeignKey(
        AudioExtra, on_delete=models.CASCADE, blank=True, null=True
    )


class AudioVisual(ItemBaseModel):
    class Status(DjangoChoices):
        damaged = ChoiceItem(_("Damaged"))
        out_of_stock = ChoiceItem(_("Out of Stock"))

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    kind = models.ForeignKey(
        Kind, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Type")
    )
    status = models.CharField(max_length=64, choices=Status, blank=True, null=True)
    is_audio_solution = models.BooleanField(default=False)
    images = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    serial_number = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.serial_number}"

    class Meta:
        indexes = [models.Index(fields=["brand"])]

    def natural_key(self):
        return self.category.name + self.category.natural_key()

    def is_damaged(self):
        return True if self.status == "damaged" else False

    def is_out_of_stock(self):
        return True if self.status == "out_of_stock" else False
