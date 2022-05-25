# Generated by Django 3.2 on 2022-05-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_question_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='previous_answer',
            new_name='previous_question',
        ),
        migrations.AddField(
            model_name='symptom',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]