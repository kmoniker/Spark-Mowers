# Generated by Django 2.0.6 on 2018-06-21 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20180621_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mailing_lists',
            field=models.ManyToManyField(blank=True, to='catalog.MailingList'),
        ),
    ]
