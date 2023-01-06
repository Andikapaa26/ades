from django.contrib import admin
from .models import *

class koordinatadmin(admin.ModelAdmin):
    list_display = ['nama_laundry', 'koordinat']
    search_fields = ['nama_laundry']
    list_per_page = 5

class laundryadmin(admin.ModelAdmin):
    list_display = ['nama_laundry', 'alamat', 'no_tlp']
    search_fields = ['nama_laundry']
    list_per_page = 5

admin.site.register(Koordinat, koordinatadmin)
admin.site.register(Laundry, laundryadmin)

# Register your models here.
