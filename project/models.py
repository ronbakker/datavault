from django.db import models

class Project(models.Model): 
    naam = models.CharField(max_length=40, blank=False,unique=True) 

    def __str__(self):
        return 'Project: {}'.format(self.naam)

    class Meta: 
        verbose_name_plural = "projecten"
