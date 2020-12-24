import os

from datavault.settings import IMPORT_CONFIG, LOGGER
from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.contrib.admin.models import ADDITION, CHANGE, LogEntry
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.http import (FileResponse, HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.utils.translation import gettext_lazy
from openpyxl import load_workbook

from glossary.models import Context, Domein, SubDomein, Term, TermType

def actionImporteerSatellieten(self, request, queryset): 
    """ 
        leest een Excel sheet met specificaties van tabellen die getruncate moeten worden 
    """
    filename = os.path.join(IMPORT_CONFIG["import"],IMPORT_CONFIG["context"]) 
    LOGGER.debug("import gestart vanuit: %s", filename)
    wb = load_workbook(filename)
    # sheetname = wb.sheetnames[1] # de tweede tab
    sheet = wb.worksheets[0]
    for row in range(2, sheet.max_row):
        contextnaam = sheet.cell(row=row, column=3).value
        domeinnaam = sheet.cell(row=row, column=11).value
        subdomeinnaam = sheet.cell(row=row, column=12).value
        # 
        context, cr2 = Context.objects.get_or_create(naam__iexact = contextnaam)
        if cr2: 
            context.naam = contextnaam
            context.save()
        if domeinnaam is not None and len(domeinnaam) > 0:           
            domein, cr4 = Domein.objects.get_or_create(naam__iexact = domeinnaam)
            if cr4: 
                domein.naam = domeinnaam
                domein.save() 
        if subdomeinnaam is not None and len(subdomeinnaam) > 0: 
            subdomein, cr5 = SubDomein.objects.get_or_create(naam__iexact = subdomeinnaam)
            if cr5: 
                subdomein.naam = subdomeinnaam
                subdomein.domein = domein
                subdomein.save()
        # table.saveTable(request.user, CHANGE) 
    LOGGER.debug("lijst met contexts geimporteerd")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])     

actionImporteerSatellieten.short_description = "importeer satellieten vanuit Excel"

def actionImporteerBegrippenlijst(self, request, queryset): 
    """ 
        leest een Excel sheet met specificaties van tabellen die getruncate moeten worden 
    """
    filename = os.path.join(IMPORT_CONFIG["import"],IMPORT_CONFIG["context"]) 
    LOGGER.debug("import gestart vanuit: %s", filename)
    wb = load_workbook(filename)
    # sheetname = wb.sheetnames[1] # de tweede tab
    sheet = wb.worksheets[0]
    for row in range(2, sheet.max_row):
        naam = sheet.cell(row=row,column=1).value
        if naam is None or len(naam) == 0: 
            continue
        termid = sheet.cell(row=row, column=2).value
        contextnaam = sheet.cell(row=row, column=3).value
        typeterm = sheet.cell(row=row, column=4).value
        eenheid = sheet.cell(row=row, column=5).value
        synoniem = sheet.cell(row=row, column=6).value 
        definitie = sheet.cell(row=row, column=7).value
        toelichting = sheet.cell(row=row, column=8).value
        domeinnaam = sheet.cell(row=row, column=11).value
        subdomeinnaam = sheet.cell(row=row, column=12).value
        # 
        context, cr2 = Context.objects.get_or_create(naam__iexact = contextnaam)
        if cr2: 
            context.naam = contextnaam
            context.save()
        termType, cr3 = TermType.objects.get_or_create(naam__iexact = typeterm)
        if cr3: 
            termType.naam = typeterm
            termType.save()   
        if domeinnaam is not None and len(domeinnaam) > 0:           
            domein, cr4 = Domein.objects.get_or_create(naam__iexact = domeinnaam)
            if cr4: 
                domein.naam = domeinnaam
                domein.save() 
            if subdomeinnaam is not None and len(subdomeinnaam) > 0: 
                subdomein, cr5 = SubDomein.objects.get_or_create(naam__iexact = subdomeinnaam)
                if cr5: 
                    subdomein.naam = subdomeinnaam
                    subdomein.domein = domein
                    subdomein.save()
        term, created = Term.objects.get_or_create(id = termid)
        if created: 
            term.id = termid
            term.naam = naam
            term.eenheid = eenheid
            term.synoniem = synoniem
            term.definitie = definitie
            term.toelichting = toelichting
            # koppel de foreign keys
            term.termType = termType
            term.context = context
            term.domein = domein
            term.subdomein = subdomein
            term.save() 
    LOGGER.debug("lijst met contexts geimporteerd")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])     

actionImporteerBegrippenlijst.short_description = "importeer Begrippenlijst"

class GlossarySite(AdminSite): 
    site_header = gettext_lazy("Architectuur, Security en Beleid <Beheer Site>")

#de admin-site voor het project 
glossary_admin = GlossarySite(name="Woordenboek")

glossary_admin.add_action(actionImporteerBegrippenlijst)
glossary_admin.add_action(actionImporteerSatellieten)

@admin.register(Domein, site=glossary_admin)
class DomeinAdmin(admin.ModelAdmin): 
    list_display = ("naam", )

@admin.register(Term, site=glossary_admin)
class TermAdmin(admin.ModelAdmin):

    list_display = ("naam", "context", "domein", "termType", )
    list_filter = ("termType", "context", "domein", "eenheid", ) 
    search_fields = ("definitie", "toelichting",) 

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
