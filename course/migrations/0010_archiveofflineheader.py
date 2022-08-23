# Generated by Django 4.1 on 2022-08-23 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0009_coursedays"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArchiveOfflineHeader",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100, null=True)),
                ("description", models.CharField(max_length=500, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "courseID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.course",
                    ),
                ),
            ],
        ),
    ]
