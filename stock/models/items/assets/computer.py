import os

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from djchoices import DjangoChoices, ChoiceItem

from access_control.models import Employee
from stock.models.items.assets.base import ItemBaseModel


def get_upload_path(instance, filename):
    return os.path.join(
        f"media/{instance}/", now().date().strftime("%Y/%m/%d"), filename
    )


class ComputerQueryset(models.QuerySet):
    def mac_computers(self):
        return self.filter(os="macOS")


class ComputerManager(models.Manager):
    def get_queryset(self):
        return ComputerQueryset(self.model, using=self._db)

    def mac_computers(self):
        return self.get_queryset().mac_computers()


class Details(ItemBaseModel):
    assigned_employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, verbose_name=_("Assigned Employee")
    )
    assigned_date = models.DateField(verbose_name=_("Date assigned"))
    returned_date = models.DateField(verbose_name=_("Date returned"))
    model = models.CharField(max_length=32, null=True, blank=True)
    model_number = models.CharField(
        verbose_name=_("Model number"), null=True, blank=True
    )
    serial_number = models.CharField(
        max_length=32, null=True, blank=True, verbose_name=_("Serial number")
    )
    warrant_expiry_date = models.DateField(
        verbose_name=_("Date of Warrant Expiry"), null=True, blank=True
    )


class Image(models.Model):
    computer = models.ForeignKey(
        "Computer",
        related_name="images",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    file = models.ImageField(blank=True, upload_to=get_upload_path, null=True)
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.computer.details.name} - {self.computer.type} - {self.computer.details.serial_number}"


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
        "Details", on_delete=models.CASCADE, related_name="computers"
    )
    os = models.CharField(choices=OsTypesChoices)
    type = models.CharField(choices=TypeChoices)

    computers = ComputerManager()

    def __str__(self):
        return self.os


class Peripheral(models.Model):
    details = models.ForeignKey(
        "Details",
        on_delete=models.CASCADE,
        related_name="peripherals",
        blank=True,
        null=True,
    )
    computer = models.ForeignKey(
        "Computer",
        on_delete=models.CASCADE,
        related_name="peripherals",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.details.name
