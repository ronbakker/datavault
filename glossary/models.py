from django.db import models

class Context(models.Model): 
    naam = models.CharField(max_length=60)

class Term(models.Model): 
    id = models.CharField(max_length=20,primary_key=True)
    naam = models.CharField(max_length=40, blank=False,unique=True) 
