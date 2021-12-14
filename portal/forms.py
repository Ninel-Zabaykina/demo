from django import forms
from .models import Portal


class AppForm(forms.ModelForm):

    class Meta:
        model = Portal
        fields = ('title', 'body',)