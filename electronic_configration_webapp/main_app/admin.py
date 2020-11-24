from django.contrib import admin
from .models import ContactUs
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(ContactUs)
class VContactUsAdmin(ImportExportModelAdmin):
    list_display = ("name", "email")
    