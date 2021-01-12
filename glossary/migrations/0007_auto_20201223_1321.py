# Generated by Django 3.1.4 on 2020-12-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0006_auto_20201223_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='eenheid',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='term',
            name='synoniem',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.CreateModel(
            name='SubDomein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=60)),
                ('domein', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='glossary.domein')),
            ],
        ),
        migrations.AddField(
            model_name='term',
            name='subdomein',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='glossary.subdomein'),
        ),
    ]