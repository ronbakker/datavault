# Generated by Django 3.1.4 on 2020-12-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('vault', '0006_auto_20201214_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='projects',
            field=models.ManyToManyField(related_name='projects', to='project.Project'),
        ),
    ]
