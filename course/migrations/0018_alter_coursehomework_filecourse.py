# Generated by Django 4.0.6 on 2022-09-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_remove_archiveofflineheader_courseid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursehomework',
            name='fileCourse',
            field=models.FileField(blank=True, null=True, upload_to='upload_course/'),
        ),
    ]
