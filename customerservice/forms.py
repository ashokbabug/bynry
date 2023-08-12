from django import forms
from .models import *

class ProblemCreationForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['problem_type','problem_description','attachment']