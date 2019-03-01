from django.db import models


class ComputerQueryset(models.QuerySet):
    def mac_computers(self):
        return self.filter(os="macOS")

    def window_computers(self):
        return self.filter(os="WindowsOS")


class ComputerManager(models.Manager):
    def get_queryset(self):
        return ComputerQueryset(self.model, using=self._db)

    def mac_computers(self):
        return self.get_queryset().mac_computers()

    def windows_computers(self):
        return self.get_queryset().window_computers()
