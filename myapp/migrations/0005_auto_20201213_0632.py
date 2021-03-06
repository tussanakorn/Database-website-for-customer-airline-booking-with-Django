# Generated by Django 3.0.7 on 2020-12-13 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201213_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='flight_name',
            new_name='bus_name',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='flight_number',
            new_name='dest',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='fromm',
            new_name='source',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='depert_date',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='destination_date',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='fare',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='to',
        ),
        migrations.AddField(
            model_name='bus',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 13, 6, 31, 58, 627576)),
        ),
        migrations.AddField(
            model_name='bus',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 12, 13, 6, 31, 58, 627609)),
        ),
        migrations.AlterField(
            model_name='book',
            name='source',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='nos',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='bus',
            name='rem',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
