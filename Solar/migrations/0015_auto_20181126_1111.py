# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Solar', '0014_auto_20181126_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='fecha_de_Venta',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='FechaVenta'),
        ),
    ]