# Generated by Django 2.1 on 2019-05-19 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuanLyTiecCuoi', '0003_auto_20190519_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 22, 59, 35, 70002)),
        ),
    ]
