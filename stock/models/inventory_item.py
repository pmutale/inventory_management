from django.db import models


class InventoryItem(models.Model):
    inventory = models.ForeignKey(
        "Inventory", on_delete=models.CASCADE, related_name="inventory_items"
    )


class Inventory(models.Model):
    name = models.CharField(max_length=32)
    total = models.IntegerField()
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="inventories"
    )


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
