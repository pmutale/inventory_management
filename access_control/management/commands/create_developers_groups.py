"""
Create permission groups
Create permissions (read only) to models for a set of groups
"""
import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

GROUPS = ["developers", "ambassadors", "managers"]
MODELS = [""]
PERMISSIONS = [
    "view"
]  # For now only view permission by default for all, others include add, delete, change


class Command(BaseCommand):
    help = "Creates read only default permission groups for users"

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            # For later use TODO: When models are fed and clarity on requirements is met.
            for model in MODELS:
                if not model:
                    for permission in PERMISSIONS:
                        name = "Can {} {}".format(permission, model)
                        print("Creating {}".format(name))

                        try:
                            model_add_perm = Permission.objects.get(name=name)
                        except Permission.DoesNotExist:
                            logging.warning(
                                "Permission not found with name '{}'.".format(name)
                            )
                            continue

                        new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")
