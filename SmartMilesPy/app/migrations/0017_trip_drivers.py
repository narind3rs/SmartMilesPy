# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20170524_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='drivers',
            field=models.ManyToManyField(to='app.Driver'),
        ),
    ]
