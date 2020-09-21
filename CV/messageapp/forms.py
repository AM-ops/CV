from django import forms
from .models import MessagesModel

class MessagesForm(forms.ModelForm):
    """docstring for MessagesForm."""
    class Meta:
        model = MessagesModel
        fields = ['name', 'email', 'message']
