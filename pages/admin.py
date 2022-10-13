from django.contrib import admin
from . models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ("firs_name",)
    