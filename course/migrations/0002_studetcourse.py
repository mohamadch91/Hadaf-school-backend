# Generated by Django 4.1 on 2022-08-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authen", "0004_student_department_student_grade"),
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudetCourse",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.IntegerField(blank=True, null=True)),
                ("description", models.CharField(max_length=500, null=True)),
                ("enable", models.BooleanField(default=True, null=True)),
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
                    "studentID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authen.student",
                    ),
                ),
            ],
        ),
    ]
