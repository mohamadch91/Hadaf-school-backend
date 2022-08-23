# Generated by Django 4.1 on 2022-08-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0006_coursedays"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, null=True)),
                ("sortIndex", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
