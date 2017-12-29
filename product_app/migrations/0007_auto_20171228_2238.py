# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 22:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_auto_20171228_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('SC', 'In Shoppingcart'), ('SM', 'Submitted'), ('PD', 'Paid'), ('PS', 'Processing'), ('SD', 'Shipped'), ('DD', 'Delivered')], default='SC', max_length=2),
        ),
    ]
