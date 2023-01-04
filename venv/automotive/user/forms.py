from django import forms
from .models import Login

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = Login
    #     fields = {
    #         'username',
    #         'password',
    #     }
    