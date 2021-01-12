# Generated by Django 3.1.4 on 2021-01-07 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glossary', '0018_remove_term_contactpersonen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domein',
            options={'ordering': ('naam',), 'verbose_name_plural': 'domeinen'},
        ),
        migrations.AlterModelOptions(
            name='subdomein',
            options={'ordering': ('naam',), 'verbose_name_plural': 'subdomeinen'},
        ),
        migrations.AddField(
            model_name='term',
            name='contactpersonen',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subdomein',
            name='domein',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='glossary.domein'),
        ),
    ]
