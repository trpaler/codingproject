from django import forms
from django.forms import ModelForm
from pathlib import Path
from weatherapp.models import Document

class DocumentForm(ModelForm):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

    class Meta:
        model = Document
        fields = ['date']
    
    def clean_docfile(self):
        docfile = self.cleaned_data.get('docfile')
        if (docfile.name.endswith('.csv') and \
            docfile.content_type == 'text/csv'):

            return docfile

        raise forms.ValidationError(
                'File should have a .csv extension', code='invalid')
