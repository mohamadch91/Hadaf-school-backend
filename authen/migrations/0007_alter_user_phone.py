# Generated by Django 4.0.6 on 2022-08-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0006_alter_otprequest_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
