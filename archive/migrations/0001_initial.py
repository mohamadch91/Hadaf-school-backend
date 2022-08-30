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
            name='ArchiveOfflineHeader',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('courseID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='ArchiveFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('fileArchibe', models.FileField(null=True, upload_to='upload_course/')),
                ('reated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('archiveHeaderID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='archive.archiveofflineheader')),
            ],
        ),
    ]