# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-04 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moirsintl', '0014_auto_20170704_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default=True, max_length=30000),
        ),
    ]
