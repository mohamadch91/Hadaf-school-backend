# Generated by Django 4.0.6 on 2022-08-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_coursehomework_filecourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursehomework',
            name='fileCourse',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
