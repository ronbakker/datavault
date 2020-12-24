from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.contrib.admin.models import ADDITION, CHANGE, LogEntry
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy

from project.models import Project
from vault.models import * # Hub, Link, HierarchicalLink, NonHistorisedLink, SameAsLink, Satellite 

class DataVaultSite(AdminSite): 
    site_header = gettext_lazy("Architectuur, Security en Beleid <Beheer Site>")

#de admin-site voor het project 
datavault_admin = DataVaultSite(name="DataVault")

@admin.register(Project, site=datavault_admin)
class ProjectAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

@admin.register(HubAttribute, site=datavault_admin)
class HubAttributeAdmin(admin.ModelAdmin): 
    list_display = ("naam","data_type","hub",'isSequence', )
    list_filter = ("hub",'isSequence','data_type', )

@admin.register(Hub, site=datavault_admin)
class HubAdmin(admin.ModelAdmin): 
    list_display = ("naam", "isStubHub", "get_projects", )
    list_filter = ('isStubHub', 'projects', )
    search_fields = ("naam",) 
    inlines = [
        HubAttributeInline, 
        SatelliteInline, 
    ]
    fieldsets = (
        ("Hub kenmerken", {"fields": ( ("naam", "isStubHub" ), )  } ),
        ("Extra informatie", { 'classes': ['collapse'], "fields":  ( "omschrijving", "toelichting",) } ),
    )    

@admin.register(Link, site=datavault_admin)
class LinkAdmin(admin.ModelAdmin): 
    list_display = ("naam","get_hubs","links") 
    inlines = [
        LinkAttributeInline, 
        SatelliteInline, 
    ]

""" @admin.register(HierarchicalLink, site=datavault_admin)
class HierarchicalLinkAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

@admin.register(SameAsLink, site=datavault_admin)
class SameAsLinkAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

@admin.register(NonHistorisedLink, site=datavault_admin)
class NonHistorisedLinkAdmin(admin.ModelAdmin):     
    list_display = ("naam",) 
 """
@admin.register(Satellite, site=datavault_admin)
class SatelliteAdmin(admin.ModelAdmin): 
    list_display = ("naam", "subtype", "hub", "link", ) 
    list_filter = ("subtype", "hub", "link",)
    inlines = [
        SatAttributeInline
    ]

@admin.register(LogEntry, site=datavault_admin)
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

datavault_admin.register(Group, GroupAdmin) 
datavault_admin.register(User, UserAdmin) 
