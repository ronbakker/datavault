from django.db import models
from django.contrib.auth.models import User

class GebruikersRol(models.Model): 
    naam = models.CharField(max_length=60, unique=True)
    class Meta:
        verbose_name_plural = "gebruikersrollen"

