import logging
import random
import string

from cms import api
from cms.models import User, Site, Page
from django.conf import settings
from django.core import exceptions
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from stock import constants
from stock.models.items.assets.audio_visual import ScreenType, ScreenMountingMethod

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

CHILD = constants.INVENTORY
SCREEN_TYPES = constants.SCREEN_TYPES
SCREEN_MOUNTING_METHODS = constants.SCREEN_MOUNTING_METHODS
NO_OF_PLUGINS = [""]


def add_plugins_to_page(placeholder, lang, child, item, link):
    # inventory_items = {k: INVENTORY[k] for k in list(INVENTORY.keys())}
    if child:
        api.add_plugin(placeholder, "CategoriesPlugin", lang, search_field=item)
    else:
        for aspect in CHILD:
            api.add_plugin(
                placeholder,
                "InventoryPlugin",
                lang,
                item=CHILD[aspect]["item"],
                # page_url=Page.objects.get(reverse_id=link)
            )


class Command(BaseCommand):
    """
    Create CMS pages
    Create page plugins
    Create default stuff --> Default Screen Types, Default Screen Mounting Methods
    """

    help = "Creates pages and plugins for all pages in CMS"

    def handle(self, *args, **options):

        random_string = ''.join(random.sample(string.ascii_letters, 6))
        # Run migrations
        call_command("migrate", verbosity=3, interactive=False)
        call_command(
            "createsuperuser", F"--username={random_string}", "--email=p@p.com", interactive=False
        )

        # Create default stuff
        for s_type in constants.SCREEN_TYPES.name:
            ScreenType.objects.all().delete()
            ScreenType.objects.get_or_create(name=s_type, description=s_type)

        for method in constants.SCREEN_MOUNTING_METHODS.name:
            ScreenMountingMethod.objects.all().delete()
            ScreenMountingMethod.objects.get_or_create(name=method, description=method)

        # Create Portal Page and Portal Plugins
        Page.objects.all().delete()
        lang = settings.LANGUAGE_CODE
        for item in PAGES:
            title = PAGES[item]["name"]

            # try:
            page = api.create_page(
                title,
                PAGES[item]["template"],
                lang,
            )
            page.save()
            # page.update_languages(dict(settings.LANGUAGES).keys())

            if not page.reverse_id == 'home':
                page.reverse_id = PAGES[item]["reverse_id"]
                page.save()



            # Publish Pages
            try:
                user = User.objects.first()
                # api.publish_page(page=page, user=user, language=lang)
                logger.info(page)
            except PermissionError:
                continue

            # Add Child pages for Categories
            if PAGES[item]["child"]:
                for child in CHILD:
                    title = CHILD[child]["item"]
                    # for lang in settings.LANGUAGES:
                    child_page = api.create_page(title=title, template=TEMPLATE_CONTENT, language=lang)
                    child_page.reverse_id = slugify(title)
                    child_page.node.depth = 2
                    child_page.save()

                    placeholder_child = child_page.placeholders.get(slot="categories")
                    add_plugins_to_page(
                        placeholder_child, lang, child=True, item=title, link=child_page.reverse_id
                    )
                    # api.publish_page(page=child_page, user=user, language=lang)

                    # child_page.update_languages(dict(settings.LANGUAGES).keys())
                    child_page.save()

                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Page with url {child_page.get_absolute_url()} has been created. >> {lang}"
                        )
                    )

                    if CHILD[child]['child']:
                        title_child_of = dict(CHILD[child]['child']),
                        child = api.create_page(
                            title=title_child_of[0]['name'], template=TEMPLATE_CONTENT, language=lang)

                        # child.update_languages(dict(settings.LANGUAGES).keys())
                        child.reverse_id = slugify(title_child_of)
                        child.save()

                        placeholder_child_of = child.placeholders.get(slot="category")
                        add_plugins_to_page(
                            placeholder_child_of, lang, child=True, item=title_child_of[0]['name'], link=child.reverse_id
                        )


                        # child_page.node.add_child()

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Page with url {child.get_absolute_url()} has been created. >> {lang}"
                            )
                        )
                        # api.publish_page(page=child, user=user, language=lang)

                    try:
                        page.set_tree_node(site=Site.objects.first())
                        child_page.move_page(target_node=page)
                        child.move_page(target_node=child_page)
                    except AssertionError:
                        continue

                    logger.info(f"A child page{child_page} has been created for {page}")

            placeholder = page.placeholders.get(slot=PAGES[item]["slot"])
            add_plugins_to_page(placeholder, lang, child=False, item=title, link=page.reverse_id)
            page.set_as_homepage() if PAGES[item]["home"] else None

            self.stdout.write(
                self.style.SUCCESS(
                    f"Page with url {page.get_absolute_url()} has been created."
                )
            )
