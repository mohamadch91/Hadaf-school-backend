# Generated by Django 4.0.6 on 2022-09-01 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='reated_at',
            new_name='created_at',
        ),
    ]
