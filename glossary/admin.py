from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.contrib.admin.models import ADDITION, CHANGE, LogEntry
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy

from glossary.models import Context, Term

class GlossarySite(AdminSite): 
    site_header = gettext_lazy("AUMC - ASB - Glossary")

#de admin-site voor het project 
glossary_admin = GlossarySite(name="Woordenboek")

@admin.register(Term, site=glossary_admin)
class TermAdmin(admin.ModelAdmin): 
    list_display = ("naam",) 

@admin.register(Context, site=glossary_admin)
class ContextAdmin(admin.ModelAdmin): 
    list_display = ('naam',)

@admin.register(LogEntry, site=glossary_admin)
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

glossary_admin.register(Group, GroupAdmin) 
glossary_admin.register(User, UserAdmin) 
