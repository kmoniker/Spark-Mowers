# Generated by Django 2.0.6 on 2018-06-22 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallengineclasses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_updates',
            field=models.BooleanField(default=False),
        ),
    ]