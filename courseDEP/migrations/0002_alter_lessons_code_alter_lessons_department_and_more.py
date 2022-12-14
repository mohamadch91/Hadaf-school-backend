# Generated by Django 4.0.6 on 2022-09-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseDEP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courseDEP.department'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courseDEP.grade'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
