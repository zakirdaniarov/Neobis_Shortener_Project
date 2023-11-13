from django import forms
from .models import Link

class UrlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['original_url']
