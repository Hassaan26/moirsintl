# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-27 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moirsintl', '0006_auto_20161227_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyintro',
            options={'verbose_name': 'Company Detail', 'verbose_name_plural': 'Company Detail'},
        ),
        migrations.AlterField(
            model_name='companyintro',
            name='company_intro',
            field=models.TextField(max_length=20000, verbose_name='Company Detail'),
        ),
    ]
