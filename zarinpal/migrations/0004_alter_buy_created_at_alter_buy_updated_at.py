# Generated by Django 4.0.6 on 2022-09-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zarinpal', '0003_buy_type_alter_buy_created_at_alter_buy_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='buy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
