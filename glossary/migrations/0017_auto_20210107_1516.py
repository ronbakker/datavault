# Generated by Django 3.1.4 on 2021-01-07 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glossary', '0016_auto_20210107_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='contactpersonen',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
