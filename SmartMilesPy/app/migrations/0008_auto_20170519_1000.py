# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170518_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odometer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.CharField(choices=[('miles', 'Miles'), ('kms', 'Kilometers')], default='kms', max_length=16)),
                ('reading', models.IntegerField()),
                ('reading_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='truck',
            name='warranty',
        ),
    ]
