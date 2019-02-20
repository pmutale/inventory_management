from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.CASCADE,
                                   null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Department(models.Model):
    name = models.CharField(max_length=68)
    team = models.ForeignKey("Team", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=68)
    field_manager = models.ForeignKey("FieldManager", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class FieldManager(models.Model):
    user = models.ForeignKey("Employee", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.user.get_full_name()
