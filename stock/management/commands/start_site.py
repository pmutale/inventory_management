import logging
import random
import string

from cms import api
from cms.models import User, Site, Page
from django.conf import settings
from django.core import exceptions
from django.core.management import call_command
from django.core.management.base import BaseCommand

from stock.constants import INVENTORY, image

logger = logging.getLogger(__name__)

TEMPLATE_MAIN = "theme/pages/portal.html"
TEMPLATE_CONTENT = "theme/pages/content.html"

PAGES = dict(
    portal=dict(
        name="Portal",
        template=TEMPLATE_MAIN,
        slot="inventories",
        home=True,
        child=False,
        reverse_id="home",
    ),
    categories=dict(
        name="Categories",
        template=TEMPLATE_CONTENT,
        slot="categories",
        child=True,
        home=False,
        reverse_id="categories",
    ),
)

CHILD = INVENTORY

DEFAULT_LANG = settings.LANGUAGE_CODE

NO_OF_PLUGINS = [""]


def add_plugins_to_page(placeholder, lang, child, item):
    # inventory_items = {k: INVENTORY[k] for k in list(INVENTORY.keys())}
    if child:
        api.add_plugin(placeholder, "CategoriesPlugin", lang, search_field=item)
    else:
        for aspect in INVENTORY:
            api.add_plugin(
                placeholder,
                "InventoryPlugin",
                lang,
                item=INVENTORY[aspect]["item"],
                image=image,
            )


class Command(BaseCommand):
    """
    Create CMS pages
    Create page plugins
    """

    help = "Creates pages and plugins for all pages in CMS"

    def handle(self, *args, **options):

        random_string = ''.join(random.sample(string.ascii_letters, 6))
        # Run migrations
        call_command("migrate", verbosity=3, interactive=False)
        call_command(
            "createsuperuser", F"--username={random_string}", "--email=p@p.com", interactive=False
        )

        # Create Portal Page and Portal Plugins
        Page.objects.all().delete()
        for item in PAGES:
            title = PAGES[item]["name"]
            try:
                page = api.create_page(
                    title,
                    PAGES[item]["template"],
                    DEFAULT_LANG,
                    reverse_id=PAGES[item]["reverse_id"],
                )
            except exceptions.FieldError:
                continue

            placeholder = page.placeholders.get(slot=PAGES[item]["slot"])
            add_plugins_to_page(placeholder, DEFAULT_LANG, child=False, item=title)
            page.set_as_homepage() if PAGES[item]["home"] else None

            # Publish Pages
            try:
                user = User.objects.first()
                api.publish_page(page=page, user=user, language=DEFAULT_LANG)
                logger.info(page)
            except PermissionError:
                continue

            # Add Child pages for Categories
            if PAGES[item]["child"]:
                for child in CHILD:
                    title = CHILD[child]["item"]
                    child_page = api.create_page(title, TEMPLATE_CONTENT, DEFAULT_LANG)
                    child_page.node.depth = 2
                    child_page.save()
                    placeholder_child = child_page.placeholders.get(slot="categories")
                    add_plugins_to_page(
                        placeholder_child, DEFAULT_LANG, child=True, item=title
                    )
                    try:
                        page.set_tree_node(site=Site.objects.first())
                        child_page.move_page(target_node=page)
                    except AssertionError:
                        continue

                    logger.info(f"A child page{child_page} has been created for {page}")

            self.stdout.write(
                self.style.SUCCESS(
                    f"Page with url {page.get_absolute_url()} has been created."
                )
            )
