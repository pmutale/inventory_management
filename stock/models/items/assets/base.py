from django.db import models
from django.db.transaction import atomic


def get_unique_slug(__cl, __param, __name):
    return f"{__cl}-{__param}-{__name}"


class ItemBaseModel(models.Model):
    quantity = models.IntegerField(null=True, blank=True)
    reorder_quantity = models.IntegerField(null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    vendor = models.CharField(null=True, blank=True)
    description = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    tags = models.CharField(max_length=32)
    purchase_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(null=True, blank=True)
    slug = models.CharField(max_length=32, null=True, blank=True)

    with atomic():

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = get_unique_slug(self.__class__, "slug", self.name)
            super().save(*args, **kwargs)
