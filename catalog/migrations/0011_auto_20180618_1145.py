# Generated by Django 2.0.6 on 2018-06-18 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20180618_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forsale',
            name='brand',
        ),
        migrations.AddField(
            model_name='forsale',
            name='description',
            field=models.TextField(default='null', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forsale',
            name='lawn_mower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.LawnMower'),
        ),
    ]
