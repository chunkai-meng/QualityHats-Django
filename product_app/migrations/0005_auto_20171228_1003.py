# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 10:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_auto_20171227_0911'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShoppingCart',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='CartItem',
            new_name='OrderItem',
        ),
    ]