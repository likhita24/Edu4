from django import forms

from .models import application

class appl_info_form(forms.ModelForm):
    class Meta:
        model = application
        fields = '__all__'
        