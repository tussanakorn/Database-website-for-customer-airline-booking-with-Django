# Generated by Django 3.0.7 on 2020-12-13 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201213_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 13, 6, 32, 47, 676216)),
        ),
        migrations.AlterField(
            model_name='bus',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 13, 6, 32, 47, 676252)),
        ),
    ]