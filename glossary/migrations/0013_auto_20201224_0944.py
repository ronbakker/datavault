# Generated by Django 3.1.4 on 2020-12-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0012_auto_20201223_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domein',
            options={'verbose_name_plural': 'domeinen'},
        ),
        migrations.AlterModelOptions(
            name='subdomein',
            options={'verbose_name_plural': 'subdomeinen'},
        ),
    ]