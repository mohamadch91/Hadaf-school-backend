# Generated by Django 4.0.6 on 2022-09-17 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_remove_quizquestion_answer1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='header_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizheader'),
        ),
    ]
