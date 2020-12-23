from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from project.models import Project

class HubAttribute(models.Model): 
    #attributen
    naam = models.CharField(max_length=40, blank=False,unique=True) 
    data_type = models.CharField(max_length=40, blank=True) 
    isSequence = models.BooleanField(verbose_name="sequence_id?",default=False) 
    # relaties 
    hub = models.ForeignKey("Hub", on_delete=models.CASCADE)
    def __str__(self): 
        return "Attr: {}".format(self.naam)
    class Meta: 
        ordering = ('-isSequence','naam',)
        verbose_name = "Attribuut (Hub)"
        verbose_name_plural = "Attributen (Hub)"


class HubAttributeInline(admin.TabularInline): 
    model = HubAttribute
    extra = 1 

class Hub(models.Model): 
    naam = models.CharField(max_length=40, blank=False,unique=True) 
    omschrijving = models.TextField(blank=True, default="")
    toelichting = models.TextField(blank=True, default="") 
    isStubHub = models.BooleanField(verbose_name="stub-hub?", default=False) 

    # relaties 
    projects = models.ManyToManyField(Project, related_name="projects")
    def __str__(self):
        return 'Hub: {}'.format(self.naam)
    def get_projects(self):
        return "\n".join([p.naam for p in self.projects.all()])
    
    class Meta: 
        ordering = ('naam', )

class LinkAttribute(models.Model): 
    #attributen
    naam = models.CharField(max_length=40, blank=False,unique=True) 
    data_type = models.CharField(max_length=40, blank=True) 
    isForeignkey = models.BooleanField(verbose_name="foreign key?", default=False)
    # relaties 
    link = models.ForeignKey("Link", on_delete=models.CASCADE)
    class Meta: 
        ordering = ('naam',)
        verbose_name = "Attribuut (Link)"
        verbose_name_plural = "Attributen (Link)"


class LinkAttributeInline(admin.TabularInline): 
    model = LinkAttribute
    extra = 1 

class Link(models.Model): 
    #attributen
    naam = models.CharField(max_length=40, blank=False,unique=True) 
    omschrijving = models.TextField(blank=True)
    # relaties 
    links = models.ForeignKey('self',blank=True, null=True, on_delete=models.CASCADE) 
    hubs  = models.ManyToManyField(Hub)

    def __str__(self): 
        return "Link: {}".format(self.naam)

    def get_hubs(self): 
        return ", ".join([h.naam for h in self.hubs.all()] )
    class Meta: 
        ordering = ('naam', )

class LinkInline(admin.TabularInline): 
    model = Link 
    extra = 1 

class HierarchicalLink(Link): 
    extra = models.TextField(blank=True, null=True)
    # 
            
class SameAsLink(Link): 
    extra = models.TextField(blank=True, null=True)
    #

class NonHistorisedLink(Link): 
    extra = models.TextField(blank=True, null=True)

class SatAttribute(models.Model): 
    #attributen
    naam = models.CharField(max_length=40, blank=False,unique=True) 
    data_type = models.CharField(max_length=40, blank=True) 
    isForeignkey = models.BooleanField(verbose_name="foreign key?", default=False)
    # relaties 
    satellite = models.ForeignKey("Satellite", on_delete=models.CASCADE)
    class Meta: 
        ordering = ('naam',)
        verbose_name = "Attribuut (Sat)"
        verbose_name_plural = "Attributen (Sat)"

class SatAttributeInline(admin.TabularInline): 
    model = SatAttribute
    extra = 1 
    
class Satellite(models.Model): 

    class Subtype(models.TextChoices):
        MULTI_ACTIVE_SATELLITE = 'MAS', _('Multi-Active')
        EFFECTIVITY_SATELLITE = 'EFF', _('Effectivity')
        SYSTEM_DRIVEN_SATELLITE = 'SYS', _('System-Driven') 

    naam = models.CharField(max_length=40, blank=False,unique=True) 
    subtype = models.CharField( max_length=3, choices=Subtype.choices, default=Subtype.SYSTEM_DRIVEN_SATELLITE )    
    # een sateliet kan attribute bevatten van zowel hubs (meestal) als van links (af en toe...)
    hub = models.ForeignKey(Hub, blank=True, null=True, on_delete=models.CASCADE) 
    link = models.ForeignKey(Link,blank=True,null=True, on_delete=models.CASCADE)

    def __str(self): 
        return 'Sat: {}'.format(self.naam)

    class Meta: 
        ordering = ('naam',)

class SatelliteInline(admin.TabularInline): 
    model = Satellite 
    extra = 1 


