from django.contrib import admin
from .models import *
# Register your models here.


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Phone, PhoneAdmin)