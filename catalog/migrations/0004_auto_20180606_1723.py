# Generated by Django 2.0.6 on 2018-06-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180606_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='description',
            field=models.CharField(blank=True, help_text='what it includes', max_length=2000),
        ),
        migrations.AlterField(
            model_name='lawnmower',
            name='service_record',
            field=models.ManyToManyField(blank=True, to='catalog.ServiceInstance'),
        ),
    ]
