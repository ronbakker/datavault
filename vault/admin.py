from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.contrib.admin.models import ADDITION, CHANGE, LogEntry
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy

from project.models import Project
from vault.models import Hub, Link, HierarchicalLink, NonHistorisedLink, SameAsLink, Satellite 

# Register your models here.

class DataVaultSite(AdminSite): 
    site_header = gettext_lazy("AUMC - ASB - Datavault")

class ProjectAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

class HubAdmin(admin.ModelAdmin): 
    list_display = ("naam","get_projects", )
    search_fields = ("naam",) 

class LinkAdmin(admin.ModelAdmin): 
    list_display = ("naam","get_hubs",) 

class HierarchicalLinkAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

class SameAsLinkAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

class NonHistorisedLinkAdmin(admin.ModelAdmin):     
    list_display = ("naam",) 

class SatelliteAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]

#de admin-site voor het project 
datavault_admin = DataVaultSite(name="DataVault")

# authorisatie en gebruikers
datavault_admin.register(Group, GroupAdmin)
datavault_admin.register(User, UserAdmin)

# logging van activiteiten per gebruikersgroep
datavault_admin.register(LogEntry,LogEntryAdmin)

# configuratie van de projecten
datavault_admin.register(Project,ProjectAdmin)
# configuratie van de Datavault-app, vooral de <Model>s
@admin.register(Hub, Link, NonHistorisedLinkAdmin, HierarchicalLink, SameAsLinkAdmin, site=datavault_admin)

""" 
datavault_admin.register(Hub,HubAdmin)
datavault_admin.register(Link, LinkAdmin)
datavault_admin.register(NonHistorisedLink, NonHistorisedLinkAdmin)
datavault_admin.register(HierarchicalLink, HierarchicalLinkAdmin)
datavault_admin.register(SameAsLink, SameAsLinkAdmin)
datavault_admin.register(Satellite, SatelliteAdmin)

"""

