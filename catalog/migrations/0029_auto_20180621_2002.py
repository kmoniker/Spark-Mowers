# Generated by Django 2.0.6 on 2018-06-22 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_auto_20180621_1859'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SmallEngineClass',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='mailing_lists',
        ),
        migrations.DeleteModel(
            name='MailingList',
        ),
    ]
