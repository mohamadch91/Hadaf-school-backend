# Generated by Django 4.0.6 on 2022-09-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quizheader_min_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizheader',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
