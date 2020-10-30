from django import forms
from .models import *

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Image
        fields='__all__'