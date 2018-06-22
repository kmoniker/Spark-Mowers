# Generated by Django 2.0.6 on 2018-06-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20180621_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='mailing_lists',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.MailingList'),
        ),
    ]
