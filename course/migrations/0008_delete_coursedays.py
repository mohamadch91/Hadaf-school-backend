# Generated by Django 4.1 on 2022-08-23 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0007_coursetype"),
    ]

    operations = [
        migrations.DeleteModel(name="CourseDays",),
    ]
