from django.db import models

class Hub(models.Model): 
    naam : models.TextField(blank=False,unique=True) 

class Link(models.Model): 
    naam : models.TextField(blank=False,unique=True) 

class Satellite(models.Model): 
    naam : models.TextField(blank=False,unique=True) 
