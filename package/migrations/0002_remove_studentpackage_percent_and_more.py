# Generated by Django 4.0.6 on 2022-09-05 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentpackage',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='studentpackagediscount',
            name='packageID',
        ),
    ]