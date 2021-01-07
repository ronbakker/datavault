from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy

from .models import GebruikersRol


class GebruikersSite(AdminSite): 
    site_header = gettext_lazy("Architectuur, Security en Beleid <Beheer Site>")

gebruikers_admin = GebruikersSite(name="Amsterdam UMC gebruikers")

@admin.register(GebruikersRol, site=gebruikers_admin)
class GebruikersRolAdmin(admin.ModelAdmin): 
    list_display = ("naam", )

