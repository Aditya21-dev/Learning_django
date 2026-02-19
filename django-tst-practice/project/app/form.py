from django import forms
from .models import User

class UserModels(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'email', 'phone', 'resume']
