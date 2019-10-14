from django import forms
from django.db.models import Q
from .models import Subject

class SubjectForm(forms.Form):
    year_level = forms.ChoiceField(
        label='Year Level',
        choices=Subject.YEAR_LEVEL_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    semester = forms.ChoiceField(
        label='Semester',
        choices=Subject.SEMESTER_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.none(),
        required=True,
        empty_label='Subject',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

        subject = Subject.objects.all()
        self.fields['subject'].queryset = Subject.objects.filter(
            Q(year_level='1st') &
            Q(semester='1st')
        )
