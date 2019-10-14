# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.list import ListView
from .forms import SubjectForm
from .models import Subject, ReferenceMaterial
import json

# Create your views here.
class IndexView(View):
    template_name = 'infosys/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class FindReferenceView(View):
    template_name = 'infosys/reference.html'
    form_class = SubjectForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ReferenceListView(ListView):
    template_name = 'infosys/view_references.html'

    def get_queryset(self):
        self.year_level = self.request.GET.get('year_level', None)
        self.semester = self.request.GET.get('semester', None)
        self.subject = self.request.GET.get('subject', None)
        return ReferenceMaterial.objects.filter(
            Q(subject__year_level=self.year_level) &
            Q(subject__semester=self.semester) &
            Q(subject=self.subject)
        )
    
    def get_object(self):
        return Subject.objects.get(pk=self.subject)

    def get_context_data(self, **kwargs):
        context = super(ReferenceListView, self).get_context_data(**kwargs)

        context.update({
            'subject': self.get_object(),
        })
        return context


def LoadSubjects(request):
    year_level = request.GET.get('year_level')
    semester = request.GET.get('semester')
    subjects = Subject.objects.filter(
        Q(year_level=year_level) &
        Q(semester=semester)
    ).values()
    
    return JsonResponse(list(subjects), safe=False)
    