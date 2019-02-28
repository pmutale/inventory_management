# Generated by Django 2.1.7 on 2019-02-27 13:09

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import stock.models.items.assets.computer


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("access_control", "0002_auto_20190220_1436"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryBase",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveSmallIntegerField(default=0)),
                ("reorder_quantity", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="CategoryPluginSearch",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="stock_categorypluginsearch",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                (
                    "search_field",
                    models.CharField(
                        help_text="HINT: Enter name of category for the page to find corresponding plugins",
                        max_length=128,
                        verbose_name="Search name",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="Computer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "os",
                    models.CharField(
                        choices=[("Mac", "macOS"), ("Window", "windowsOS")],
                        max_length=32,
                        verbose_name="Operating System",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Desktop", "desktop"),
                            ("Laptop", "laptop"),
                            ("Mobile", "mobile"),
                            ("Tablet", "tablet"),
                        ],
                        max_length=32,
                    ),
                ),
            ],
            managers=[("computers", django.db.models.manager.Manager())],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=stock.models.items.assets.computer.get_upload_path,
                    ),
                ),
                ("position", models.PositiveSmallIntegerField(default=0)),
                (
                    "computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="stock.Computer",
                    ),
                ),
            ],
            options={"ordering": ["position"]},
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="stock_inventory",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                (
                    "total",
                    models.IntegerField(
                        blank=True, default=0, null=True, verbose_name="Total"
                    ),
                ),
                (
                    "item",
                    models.CharField(
                        help_text="Create an item at the top level of classification",
                        max_length=128,
                        verbose_name="Item",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=stock.models.items.assets.computer.get_upload_path,
                    ),
                ),
                (
                    "page_url",
                    cms.models.fields.PageField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms.Page",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Inventories"},
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="ItemBaseModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cost", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(max_length=1024)),
                ("name", models.CharField(max_length=32)),
                ("tags", models.CharField(max_length=32)),
                ("purchase_date", models.DateField(blank=True, null=True)),
                ("is_deleted", models.BooleanField(blank=True, null=True)),
                ("slug", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Peripheral",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "computer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="peripherals",
                        to="stock.Computer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("address", models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "categorybase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="stock.CategoryBase",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Naam"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=1024,
                        null=True,
                        verbose_name="Beschrijving",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=stock.models.items.assets.computer.get_upload_path,
                    ),
                ),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="stock.Inventory",
                        verbose_name="Inventory",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Categorieën"},
            bases=("stock.categorybase",),
        ),
        migrations.CreateModel(
            name="Details",
            fields=[
                (
                    "itembasemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="stock.ItemBaseModel",
                    ),
                ),
                (
                    "assigned_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date assigned"
                    ),
                ),
                (
                    "returned_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date returned"
                    ),
                ),
                ("model", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "model_number",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Model number",
                    ),
                ),
                (
                    "serial_number",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Serial number",
                    ),
                ),
                (
                    "warrant_expiry_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of Warrant Expiry"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Details"},
            bases=("stock.itembasemodel",),
        ),
        migrations.AddField(
            model_name="vendor",
            name="item",
            field=models.ManyToManyField(to="stock.ItemBaseModel"),
        ),
        migrations.CreateModel(
            name="PeripheralDetails",
            fields=[
                (
                    "details_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="stock.Details",
                    ),
                ),
                ("is_peripheral", models.BooleanField(default=True)),
            ],
            bases=("stock.details",),
        ),
        migrations.AddField(
            model_name="details",
            name="assigned_employee",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="access_control.Employee",
                verbose_name="Assigned Employee",
            ),
        ),
        migrations.AddField(
            model_name="computer",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computers",
                to="stock.Category",
            ),
        ),
        migrations.AddField(
            model_name="computer",
            name="details",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computers",
                to="stock.Details",
            ),
        ),
        migrations.AddField(
            model_name="peripheral",
            name="details",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="peripherals",
                to="stock.PeripheralDetails",
                verbose_name="Peripheral Details",
            ),
        ),
    ]