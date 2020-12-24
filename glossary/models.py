from django.db import models
from django.utils.translation import gettext_lazy as _

class Domein (models.Model): 
    naam = models.CharField(max_length=60)

    def __str__(self):
        return self.naam
    class Meta: 
        verbose_name_plural = "domeinen"


class SubDomein(models.Model): 
    naam = models.CharField(max_length=60)
    domein = models.ForeignKey(Domein, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.naam
    class Meta: 
        verbose_name_plural = "subdomeinen"

class Context(models.Model): 
    naam = models.CharField(max_length=60)

    def __str__(self):
        return self.naam

    class Meta: 
        ordering = ('naam',)
        verbose_name_plural = "contexten"


class TermType(models.Model): 
    naam = models.CharField(max_length=20,primary_key=True)

    def __str__(self): 
        return self.naam 

class Term(models.Model): 
    class TermType(models.TextChoices):
        BEGRIP = 'BEGRIP', _('Begrip')
        DEFINITIE  = 'DEFINITIE', _('DEFINITIE')

    id = models.CharField(max_length=20, primary_key=True)
    naam = models.CharField(max_length=40, blank=False,null=False) 
    synoniem = models.CharField(max_length=40, blank=True,null=True)
    termType = models.CharField( max_length=10, choices=TermType.choices, default=TermType.BEGRIP) 
    eenheid = models.CharField(max_length=50, blank=True, null=True)
    definitie = models.TextField(blank=True, null=True)
    toelichting = models.TextField(blank=True, null=True)

    # relaties 
    context   = models.ForeignKey("Context", on_delete=models.DO_NOTHING, blank=True, null=True)
    domein    = models.ForeignKey("Domein", on_delete=models.DO_NOTHING, blank=True, null=True)
    termType  = models.ForeignKey("TermType", on_delete=models.DO_NOTHING, blank=True, null=True) 
    domein    = models.ForeignKey("Domein", on_delete=models.DO_NOTHING, blank=True, null=True)
    subdomein = models.ForeignKey("SubDomein", on_delete=models.DO_NOTHING, blank=True, null=True) 

    def __str__(self):
        return self.naam

    class Meta: 
        ordering = ('naam', )
        verbose_name_plural = "termen"
        
