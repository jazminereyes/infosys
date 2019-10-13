# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_name', models.CharField(max_length=200)),
                ('reference_author', models.CharField(blank=True, max_length=200)),
                ('reference_type', models.CharField(choices=[('pdf', 'PDF'), ('link', 'Link'), ('ppt', 'Powerpoint')], max_length=10)),
                ('reference_material', models.FileField(blank=True, upload_to='materials/')),
                ('reference_text', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('year_level', models.CharField(choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year'), ('5th', '5th year')], max_length=50)),
                ('semester', models.CharField(choices=[('1st', '1st Semester'), ('2nd', '2nd Semester')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='referencematerial',
            name='subject_name',
            field=models.ManyToManyField(blank=True, to='referencematerial.Subject'),
        ),
    ]