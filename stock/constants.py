import os
from collections import namedtuple
from PIL import Image

from django.utils.translation import gettext as _
from easy_thumbnails.files import get_thumbnailer

from settings import BASE_DIR

INVENTORY = {
    "audio_visual": {
        "item": _("Audiovisual Equipment"),
        "child": [("name", _("All Audio Visual")), ],
    },
    "computers": {
        "item": _("Computer and Media supplies"),
        "child": [("name", _("All Computer and Media Supplies")), ],
    },
    "print_material": {
        "item": _("Ink and Catridges"),
        "child": [("name", _("All Ink and Catridges")), ],
    },
    "cleaning_stuf": {
        "item": _("Office Cleaning"),
        "child": [("name", _("All Office Cleaning")), ],
    },
}

default_foto = "theme/static/theme/images/_49A2386.jpg"

# default_foto.thumbnail(20, 20)
# default_foto.save()
url = Image.open(os.path.join(BASE_DIR, default_foto))
url.thumbnail((341, 227))

image = url

URL = dict(audio_visual="audio_visual", computer="computer")
SCREEN = {
    "SCREEN_TYPES": {"name": "", "desc": ""},
    "SCREEN_MOUNTING_METHODS": {"name": "", "desc": ""},
}

SCREEN_TYPES = namedtuple("ScreenTypes", "name description")
SCREEN_MOUNTING_METHODS = namedtuple("ScreenMethods", "name description")
SCREEN_TYPES.name = [_("LCD"), _("LED"), "AM0LED", "Vinyl", "Vinyl Matt"]
SCREEN_MOUNTING_METHODS.name = [_("Tripod"), _("Wall Mounted")]
