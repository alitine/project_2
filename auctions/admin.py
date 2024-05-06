from .models import Listing
from django.contrib import admin

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "comment", "price", "category")

# Register your models here.
admin.site.register(Listing, ListingAdmin)