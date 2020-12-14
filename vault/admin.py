from django.contrib.admin import AdminSite
from django.contrib import admin
from django.utils.translation import gettext_lazy

from vault.models import Hub, Link, Satellite

# Register your models here.

class DataVaultSite(AdminSite): 
    site_header = gettext_lazy("AUMC - ASB - Datavault")

class HubAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

class LinkAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

class SatelliteAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

datavault_admin = DataVaultSite(name="DataVault")
datavault_admin.register(Hub,HubAdmin)
datavault_admin.register(Link, LinkAdmin)
datavault_admin.register(Satellite, SatelliteAdmin)


