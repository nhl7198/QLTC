# Generated by Django 2.1 on 2019-05-19 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLyTiecCuoi', '0005_auto_20190519_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_at',
        ),
        migrations.AddField(
            model_name='order',
            name='at',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2019, 5, 19)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 23, 41, 47, 427876)),
        ),
    ]