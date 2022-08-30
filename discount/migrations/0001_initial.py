# Generated by Django 4.0.6 on 2022-08-23 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0017_remove_archiveofflineheader_courseid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('asDate', models.DateField(null=True)),
                ('toDate', models.DateField(null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('isPercent', models.BooleanField(default=True, null=True)),
                ('active', models.BooleanField(default=True, null=True)),
                ('reated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('discountID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discount.discount')),
            ],
        ),
    ]