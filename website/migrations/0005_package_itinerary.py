# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-01 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_package_itinerary'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='itinerary',
            field=models.CharField(default='', max_length=1000),
        ),
    ]