# Generated by Django 2.0.6 on 2018-06-18 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180617_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forsale',
            name='sale_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Customer'),
        ),
        migrations.AlterField(
            model_name='forsale',
            name='sale_price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
