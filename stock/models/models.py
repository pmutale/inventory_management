from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField

from stock.models.items.assets.base import CategoryBase
from stock.models.items.assets.computer import Details, get_upload_path
from stock.models.items.plugins.category import Inventory
from stock.models.managers.computers import ComputerManager


class Category(CategoryBase):
    name = models.CharField(
        max_length=128, blank=True, null=True, verbose_name=_("Name")
    )
    description = models.TextField(
        max_length=1024, blank=True, null=True, verbose_name=_("Description")
    )
    image = FilerImageField(blank=True, null=True, related_name="category_images", on_delete=models.CASCADE)
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        verbose_name=_("Inventory"),
        related_name="categories",
    )

    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class Computer(models.Model):
    class OsTypesChoices(DjangoChoices):
        macOS = ChoiceItem("Mac")
        windowsOS = ChoiceItem("Window")

    class TypeChoices(DjangoChoices):
        desktop = ChoiceItem("Desktop")
        laptop = ChoiceItem("Laptop")
        mobile = ChoiceItem("Mobile")
        tablet = ChoiceItem("Tablet")

    details = models.ForeignKey(
        Details, on_delete=models.CASCADE, related_name="computers"
    )
    os = models.CharField(
        choices=OsTypesChoices, max_length=32, verbose_name=_("Operating System")
    )
    image = FilerImageField(blank=True, null=True, related_name="computer_images", on_delete=models.CASCADE)
    type = models.CharField(choices=TypeChoices, max_length=32)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="computers"
    )

    computers = ComputerManager()

    def __str__(self):
        return (
            F"{self.details.name} - {self.details.model} - {self.details.model_number}"
        )
