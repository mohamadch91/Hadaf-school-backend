# Generated by Django 4.0.6 on 2022-08-23 23:00

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authen', '0007_alter_user_phone'),
        ('course', '0017_remove_archiveofflineheader_courseid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizHeader',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('quizTime', models.IntegerField(blank=True, default=0, null=True)),
                ('question_count', models.IntegerField(blank=True, default=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.expressions.Case, to='course.course')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='authen.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='quizQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, max_length=350, null=True)),
                ('answer1', models.TextField(blank=True, max_length=400, null=True)),
                ('answer2', models.TextField(blank=True, max_length=400, null=True)),
                ('answer3', models.TextField(blank=True, max_length=400, null=True)),
                ('answer4', models.TextField(blank=True, max_length=400, null=True)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('header_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizheader')),
            ],
        ),
        migrations.CreateModel(
            name='studentQueez',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('quizQuestion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizquestion')),
                ('quizheader', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizheader')),
            ],
        ),
    ]
