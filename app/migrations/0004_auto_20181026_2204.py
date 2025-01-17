# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-27 03:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181026_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 26, 22, 4, 12, 618702)),
        ),
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 26, 22, 4, 12, 618775)),
        ),
        migrations.AlterField(
            model_name='historialglobo',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 26, 22, 4, 12, 618745)),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='cantidad',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
