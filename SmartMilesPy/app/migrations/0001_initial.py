# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=64)),
                ('address_line_2', models.CharField(blank=True, max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=16)),
                ('postal_code', models.CharField(blank=True, max_length=16)),
                ('country', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='LicensePlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=16)),
                ('number', models.CharField(max_length=16)),
                ('expiration_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('make', models.CharField(max_length=16)),
                ('model', models.CharField(max_length=16)),
                ('model_year', models.IntegerField(null=True)),
                ('color', models.CharField(blank=True, max_length=16)),
                ('vin', models.CharField(blank=True, max_length=16)),
                ('purchase_date', models.DateTimeField(blank=True)),
                ('safety_expiration_date', models.DateTimeField(blank=True)),
                ('emissions_expiration_date', models.DateTimeField(blank=True)),
                ('retire_date', models.DateTimeField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('license_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='license_plate', to='app.LicensePlate')),
            ],
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_type', models.CharField(blank=True, choices=[('MN', 'Manufacturer'), ('DL', 'Dealer'), ('TP', 'Third Party')], max_length=2)),
                ('effective_date', models.DateTimeField(blank=True)),
                ('expiration_date', models.DateTimeField(blank=True)),
                ('expiry_odometer', models.CharField(blank=True, max_length=8)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarrantyAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('dba', models.CharField(blank=True, max_length=64)),
                ('contact_name', models.CharField(blank=True, max_length=64)),
                ('primary_phone', models.CharField(blank=True, max_length=16)),
                ('secondary_phone', models.CharField(blank=True, max_length=16)),
                ('fax', models.CharField(blank=True, max_length=16)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='app.Address')),
            ],
        ),
        migrations.AddField(
            model_name='warranty',
            name='warranty_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warranty_admins', to='app.WarrantyAdmin'),
        ),
        migrations.AddField(
            model_name='truck',
            name='warranty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warranties', to='app.Warranty'),
        ),
    ]
