# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solar', '0024_auto_20181128_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='estatus',
            field=models.CharField(default='Pendiente', max_length=50, null=True),
        ),
    ]
