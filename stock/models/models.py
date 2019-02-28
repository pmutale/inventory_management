from cms.models import CMSPlugin
from cms.models.fields import PageField
from cms.plugin_base import CMSPluginBase
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from django.utils.translation import gettext as _
from hvad.models import TranslatableModel, TranslatedFields

from stock.models.items.assets.base import CategoryBase
from stock.models.items.assets.computer import Details, get_upload_path
from stock.models.managers.computers import ComputerManager


class Inventory(CMSPlugin):
    total = models.IntegerField(
        blank=True, null=True, verbose_name=_("Total"), default=0
    )
    item = models.CharField(
        max_length=128,
        verbose_name=_("Item"),
        help_text=_("Create an item at the top level of classification"),
    )
    image = models.ImageField(blank=True, upload_to=get_upload_path, null=True)
    page_url = PageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Inventories")

    def __str__(self):
        return self.item

    def copy_relations(self, oldinstance):
        self.categories.all().delete()

        for category in oldinstance.categories.all():
            category.pk = category.id = None
            category.plugin = self
            category.save()


class Category(CategoryBase):
    name = models.CharField(
        max_length=128, blank=True, null=True, verbose_name=_("Name")
    )
    description = models.TextField(
        max_length=1024, blank=True, null=True, verbose_name=_("Description")
    )
    image = models.ImageField(blank=True, upload_to=get_upload_path, null=True)
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
    type = models.CharField(choices=TypeChoices, max_length=32)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="computers"
    )

    computers = ComputerManager()

    def __str__(self):
        return (
            f"{self.details.name} - {self.details.model} - {self.details.model_number}"
        )


# class Image(models.Model):
#     inventory = models.ForeignKey(
#         "Inventory",
#         related_name="images",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#     )
#     file = models.ImageField(blank=True, upload_to=get_upload_path, null=True)
#     position = models.PositiveSmallIntegerField(default=0)
#
#     class Meta:
#         ordering = ["position"]
#
#     def __str__(self):
#         return f"{self.inventory.details.name} - {self.inventory.type} - {self.inventory.details.serial_number}"
