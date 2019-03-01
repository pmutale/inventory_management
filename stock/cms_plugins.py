from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from stock.models import Category, Inventory
from stock.models.items.plugins.category import CategoryPluginSearch


class CategoryInlineAdmin(admin.StackedInline):
    model = Category
    fields = ["reorder_quantity", "name", "description", "image"]


@plugin_pool.register_plugin
class InventoryPlugin(CMSPluginBase):
    model = Inventory
    inlines = (CategoryInlineAdmin,)
    render_template = "stock/pages/inventories.html"
    cache = False
    fields = ["item", "page_url", "image"]

    def render(self, context, instance, placeholder):
        context = super(InventoryPlugin, self).render(context, instance, placeholder)
        categories = instance.categories.count()
        context.update({"categories": categories})
        return context


@plugin_pool.register_plugin
class CategoriesPlugin(CMSPluginBase):
    model = CategoryPluginSearch
    render_template = "stock/pages/categories.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(CategoriesPlugin, self).render(context, instance, placeholder)
        categories = Category.objects.all()
        context.update({"category": categories})
        return context


@plugin_pool.register_plugin
class InventoryLatestPlugin(CMSPluginBase):
    render_template = "stock/pages/inventories/latest.html"
    cache = False
    name = _("Latest Inventories")

    def render(self, context, instance, placeholder):
        context = super(InventoryLatestPlugin, self).render(
            context, instance, placeholder
        )
        latest = Inventory.objects.all()
        context.update({"latest": latest})
        return context
