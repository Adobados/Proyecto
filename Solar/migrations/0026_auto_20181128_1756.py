# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solar', '0025_auto_20181128_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='Producto',
            field=models.CharField(default='Boiler Solar 10', max_length=50, verbose_name='Producto'),
        ),
    ]