# Generated by Django 4.0.6 on 2022-09-01 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_rename_reated_at_discount_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
