# Generated by Django 2.0.6 on 2018-06-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20180620_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]