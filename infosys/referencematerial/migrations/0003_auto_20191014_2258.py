# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-14 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referencematerial', '0002_auto_20191013_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='year_level',
            field=models.CharField(choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')], max_length=50),
        ),
    ]