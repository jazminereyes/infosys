# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referencematerial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referencematerial',
            old_name='subject_name',
            new_name='subject',
        ),
    ]