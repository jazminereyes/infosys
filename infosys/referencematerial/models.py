# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ReferenceMaterial(models.Model):
    REFERENCE_TYPE_CHOICES = (
        ('pdf', 'PDF'), 
        ('link', 'Link'), 
        ('ppt', 'Powerpoint'),
    )

    reference_name = models.CharField(max_length=200)
    reference_author = models.CharField(
        max_length=200,
        blank=True
    )

    reference_type = models.CharField(
        max_length=10,
        choices=REFERENCE_TYPE_CHOICES
    )

    reference_material = models.FileField(
        blank=True,
        upload_to='materials/'
    )

    reference_text = models.CharField(
        max_length=200,
        blank=True
    )

    subject = models.ManyToManyField(
        'Subject', 
        blank=True
    )

    def __str__(self):
        return self.reference_name

class Subject(models.Model):
    YEAR_LEVEL_CHOICES = (
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    )

    SEMESTER_CHOICES = (
        ('1st', '1st Semester'),
        ('2nd', '2nd Semester'),
    )

    subject_name = models.CharField(max_length=200)
    year_level = models.CharField(
        max_length=50,
        choices=YEAR_LEVEL_CHOICES
    )

    semester = models.CharField(
        max_length=50,
        choices=SEMESTER_CHOICES
    )

    def __str__(self):
        return self.subject_name