# Generated by Django 4.0.6 on 2022-09-10 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0007_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
