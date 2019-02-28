import os

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _

from access_control.models import Employee
from stock.models.items.assets.base import ItemBaseModel


def get_upload_path(instance, filename):
    return os.path.join(
        f"media/{instance}/", now().date().strftime("%Y/%m/%d"), filename
    )


class Details(ItemBaseModel):
    assigned_employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        verbose_name=_("Assigned Employee"),
        null=True,
        blank=True,
    )
    assigned_date = models.DateField(
        verbose_name=_("Date assigned"), null=True, blank=True
    )
    returned_date = models.DateField(
        verbose_name=_("Date returned"), null=True, blank=True
    )
    model = models.CharField(max_length=128, null=True, blank=True)
    model_number = models.CharField(
        verbose_name=_("Model number"), null=True, blank=True, max_length=128
    )
    serial_number = models.CharField(
        max_length=128, null=True, blank=True, verbose_name=_("Serial number")
    )
    warrant_expiry_date = models.DateField(
        verbose_name=_("Date of Warrant Expiry"), null=True, blank=True
    )

    class Meta:
        verbose_name_plural = _("Details")

    def __str__(self):
        return f"{self.model}-{self.serial_number}"


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


class PeripheralDetails(Details):
    is_peripheral = models.BooleanField(default=True)


class Peripheral(models.Model):
    details = models.ForeignKey(
        "PeripheralDetails",
        on_delete=models.CASCADE,
        related_name="peripherals",
        blank=True,
        null=True,
        verbose_name=_("Peripheral Details"),
    )
    computer = models.ForeignKey(
        "Computer",
        on_delete=models.CASCADE,
        related_name="peripherals",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.details.name} - {self.computer.details.name} - {self.computer.details.serial_number}"
