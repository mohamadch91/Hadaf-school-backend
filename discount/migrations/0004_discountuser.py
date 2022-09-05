# Generated by Django 4.0.6 on 2022-09-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0003_alter_discount_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('family', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('percent', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
