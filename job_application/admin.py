from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Form model.

    Configures display options, search capabilities,
    and field behaviors in the Django admin.
    """
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("-date",)
    readonly_fields = ("occupation",)


# Register the Form model with the custom admin configuration
admin.site.register(Form, FormAdmin)