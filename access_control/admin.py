from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee, Department, Team, FieldManager


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    can_add = True
    verbose_name_plural = "employee"


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    can_add = True
    list_display = ("name", "team")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    can_add = True
    list_display = ("name", "field_manager")


@admin.register(FieldManager)
class FieldManagerAdmin(admin.ModelAdmin):
    can_add = True
    list_display = ("user",)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
