# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 22:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0008_auto_20171229_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
