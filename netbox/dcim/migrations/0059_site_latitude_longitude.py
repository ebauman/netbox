# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-21 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0058_relax_rack_naming_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
