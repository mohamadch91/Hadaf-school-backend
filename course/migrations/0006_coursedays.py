# Generated by Django 4.1 on 2022-08-23 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courseDEP", "0001_initial"),
        ("course", "0005_alter_coursehomework_filecourse"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseDays",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
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
                (
                    "dayID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courseDEP.days",
                    ),
                ),
            ],
        ),
    ]
