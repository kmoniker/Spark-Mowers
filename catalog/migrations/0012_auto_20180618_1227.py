# Generated by Django 2.0.6 on 2018-06-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180618_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forsale',
            name='sale_customer',
        ),
        migrations.RemoveField(
            model_name='lawnmower',
            name='serial_number',
        ),
        migrations.AlterField(
            model_name='lawnmower',
            name='chassis_model',
            field=models.CharField(blank=True, help_text='model number of the chassis', max_length=200),
        ),
        migrations.AlterField(
            model_name='lawnmower',
            name='engine_model',
            field=models.CharField(blank=True, help_text='model number of the engine', max_length=200),
        ),
    ]
