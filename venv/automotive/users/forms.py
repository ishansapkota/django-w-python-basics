from django import forms
from .models import users
from django.contrib.auth.forms import UserCreationForm,UserChangeForm   #yo chahi user create garney bela use huney django ko provided forms haru ho 
from django.contrib.auth import authenticate,login



# class UserCreationForm(UserCreationForm):

#     is_superuser = forms.BooleanField()
#     class Meta:
#         model = User
#         fields = ("username", "email", 'is_superuser')

# class UserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ("username", "email")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    
    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password')
        self.user = user
        return cleaned_data
    
    def login_user(self):
        login(self.request, self.user)
  