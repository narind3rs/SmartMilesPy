# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170519_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='odometer',
            field=models.ManyToManyField(to='app.Odometer'),
        ),
        migrations.AddField(
            model_name='truck',
            name='warranties',
            field=models.ManyToManyField(to='app.Warranty'),
        ),
    ]