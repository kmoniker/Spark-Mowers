# Generated by Django 2.0.6 on 2018-06-26 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0030_auto_20180624_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerecord',
            name='notes',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='lawnmower',
            name='chassis_model',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='lawnmower',
            name='engine_model',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='lawnmower',
            name='notes',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicerecord',
            name='cost',
            field=models.CharField(help_text='how much they paid', max_length=200),
        ),
    ]
