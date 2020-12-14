from django.db import models

class Hub(models.Model): 
    naam = models.CharField(max_length=40, blank=False,unique=True) 

class Link(models.Model): 
    naam = models.CharField(max_length=40, blank=False,unique=True) 

class Satellite(models.Model): 
    naam = models.CharField(max_length=40, blank=False,unique=True) 
