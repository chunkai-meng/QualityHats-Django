# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 23:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, default='Auckland', max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?\\d{8,16}$')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='recipient',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Recipient Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, default='New Zealand', max_length=100, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='order',
            name='submitted_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Submitted Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Price'),
        ),
    ]
