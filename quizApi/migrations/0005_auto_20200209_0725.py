# Generated by Django 2.1.5 on 2020-02-09 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizApi', '0004_auto_20200209_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApi.Question'),
        ),
    ]