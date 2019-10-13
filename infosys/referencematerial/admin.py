# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ReferenceMaterial, Subject

# Register your models here.
admin.site.register(ReferenceMaterial)
admin.site.register(Subject)