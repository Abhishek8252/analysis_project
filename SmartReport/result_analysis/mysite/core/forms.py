from django import forms

from .models import Result
from .models import AnalysisFile


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('title', 'pdf')


class AnalysisFileForm(forms.ModelForm):
    class Meta:
        model = AnalysisFile
        fields = ('title', 'excel')
