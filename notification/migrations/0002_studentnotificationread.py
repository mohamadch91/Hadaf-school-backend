# Generated by Django 4.0.6 on 2022-09-10 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0007_alter_user_phone'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentNotificationRead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('notification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.notification')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authen.student')),
            ],
        ),
    ]
