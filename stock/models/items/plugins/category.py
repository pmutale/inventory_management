from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryPluginSearch(CMSPlugin):
    search_field = models.CharField(
        max_length=128,
        verbose_name=_("Search name"),
        help_text=_(
            "HINT: Enter name of category for the page to find corresponding plugins"
        ),
    )
