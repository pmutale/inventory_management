from django.db import models
from django.db.transaction import atomic


def get_unique_slug(__cl, __param, __name):
    return f"{__cl}-{__param}-{__name}"


class ItemBaseModel(models.Model):
    cost = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=1024)
    name = models.CharField(max_length=32)
    tags = models.CharField(max_length=32)
    purchase_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(null=True, blank=True)
    slug = models.CharField(max_length=128, null=True, blank=True)

    # class Meta:
    #     abstract = True

    with atomic():

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = get_unique_slug(self.__class__, "slug", self.name)
            super().save(*args, **kwargs)


class Vendor(models.Model):
    item = models.ManyToManyField(ItemBaseModel)
    name = models.CharField(max_length=32)
    address = models.TextField(max_length=1024)

    def __str__(self):
        return self.name


class CategoryBase(models.Model):
    quantity = models.PositiveSmallIntegerField(default=0)
    reorder_quantity = models.IntegerField(null=True, blank=True)

    # class Meta:
    #     abstract = True
