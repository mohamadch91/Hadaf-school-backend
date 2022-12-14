# Generated by Django 4.1 on 2022-08-23 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0015_remove_discountcourse_courseid_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="discountcourse", name="active",),
        migrations.RemoveField(model_name="discountcourse", name="amount",),
        migrations.RemoveField(model_name="discountcourse", name="asDate",),
        migrations.RemoveField(model_name="discountcourse", name="code",),
        migrations.RemoveField(model_name="discountcourse", name="count",),
        migrations.RemoveField(model_name="discountcourse", name="isPercent",),
        migrations.RemoveField(model_name="discountcourse", name="reated_at",),
        migrations.RemoveField(model_name="discountcourse", name="toDate",),
        migrations.RemoveField(model_name="discountcourse", name="updated_at",),
        migrations.AddField(
            model_name="discountcourse",
            name="courseID",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="course.course",
            ),
        ),
        migrations.AddField(
            model_name="discountcourse",
            name="discountID",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="course.discount",
            ),
        ),
    ]
