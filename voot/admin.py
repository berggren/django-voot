"""Admin classes for voot application."""

from django.contrib import admin

from voot.models import Example


class ExampleAdmin(admin.ModelAdmin):
    """Admin class for Example model class."""
    pass


admin.site.register(Example, ExampleAdmin)
