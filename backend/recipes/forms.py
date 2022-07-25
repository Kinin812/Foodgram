from django import forms
from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet
from django.forms.widgets import TextInput

from .models import Tag


class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
                   for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('Требуется хотя бы одна запись.')


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {'color': TextInput(attrs={'type': 'color'}), }
