from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class CategoryPluginSearch(CMSPlugin):
    slug = models.SlugField(max_length=128,
                            help_text=_('This slug is used to map the URL of this category at the front end'),
                            default='example',
                            blank=True,
                            null=True
                            )
    search_field = models.CharField(
        max_length=128,
        verbose_name=_("Search name"),
        help_text=_(
            "HINT: Enter name of category for the page to find corresponding plugins"
        ),
    )
    page_url = PageField(blank=True, null=True)

    def get_slug(self):
        return F"stock:{self.slug}"


class Inventory(CMSPlugin):
    total = models.IntegerField(
        blank=True, null=True, verbose_name=_("Total"), default=0
    )
    item = models.CharField(
        max_length=128,
        verbose_name=_("Item"),
        help_text=_("Create an item at the top level of classification"),
    )
    image = FilerImageField(blank=True, null=True, related_name="inventory_images", on_delete=models.CASCADE)
    page_url = PageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Inventories")

    def __str__(self):
        return self.item

    # def copy_relations(self, oldinstance):
    #     self.categories.all().delete()
    #
    #     for category in oldinstance.categories.all():
    #         category.pk = category.id = None
    #         category.plugin = self
    #         category.save()


class CategoryPlugin(CMSPlugin):
        inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='associated_inventory_category')
        # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='associaltes_category')
