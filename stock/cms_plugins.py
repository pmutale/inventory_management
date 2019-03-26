from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

import plotly.offline as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

from stock.models import Category, Inventory, CategoryPlugin, CategoryPluginSearch


class CategoryInlineAdmin(admin.StackedInline):
    model = Category
    fields = ["reorder_quantity", "name", "description", "image"]


@plugin_pool.register_plugin
class InventoryPlugin(CMSPluginBase):
    model = Inventory
    module = _('Stock')
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
    module = _('Stock')
    render_template = "stock/pages/categories.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(CategoriesPlugin, self).render(context, instance, placeholder)
        categories = Category.objects.all()
        context.update({"category": categories, 'instance': instance})
        return context


@plugin_pool.register_plugin
class CategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    module = _('Stock')
    render_template = "stock/pages/category.html"
    cache = False

    def render(self, context, instance, placeholder):
        category = instance.inventory.categories.all()
        context = super(CategoryPlugin, self).render(context, instance, placeholder)

        labels = list(category.values_list("name", flat=True))
        values = []
        products = {}

        for item in category:
            products[item.name] = item.audio_visuals.values('name', 'purchase_date', 'serial_number')
            values.append(item.audio_visuals.count())

        trace = go.Pie(
            labels=labels,
            values=values,
            hoverinfo="label+percent",
            textinfo="value",
            textfont=dict(size=18),
            marker=dict(line=dict(color="#000000", width=1)),
        )

        graph = py.plot([trace], output_type="div")

        df = pd.DataFrame({
            "x": labels,
            "y": values
        })
        df.head()

        data = [go.Bar(x=df["x"], y=df["y"])]
        url = py.plot(data, output_type="div")

        context["graph"] = graph
        context["graph_bar"] = url
        context['product'] = products
        return context


@plugin_pool.register_plugin
class InventoryLatestPlugin(CMSPluginBase):
    render_template = "stock/pages/inventories/latest.html"
    module = _('Stock')
    cache = False
    name = _("Latest Inventories")

    def render(self, context, instance, placeholder):
        context = super(InventoryLatestPlugin, self).render(
            context, instance, placeholder
        )
        latest = Inventory.objects.all()
        context.update({"latest": latest})
        return context
