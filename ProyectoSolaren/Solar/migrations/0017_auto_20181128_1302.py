# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solar', '0016_ventas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='Cantidad',
        ),
        migrations.AddField(
            model_name='ventas',
            name='Numero_de_Telefono',
            field=models.CharField(default=False, max_length=50, verbose_name='Numero'),
        ),
    ]
