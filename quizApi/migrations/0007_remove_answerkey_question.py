# Generated by Django 2.1.5 on 2020-02-14 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApi', '0006_auto_20200210_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerkey',
            name='question',
        ),
    ]