from django import forms
from .models import User

class UserModels(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'email', 'phone', 'password' , 'resume']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()