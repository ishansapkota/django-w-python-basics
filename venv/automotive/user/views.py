from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserChangeForm,UserCreationForm
from django.http import HttpResponse
from django.views import View
from django.urls import reverse


# Create your views here.

# class RegistrationView(View):

#     def get(self, request):
#         context = {'form': UserCreationForm()}
#         return render(request, 'users/register.html', context)

#     def post(self, request, *args, **kwargs):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             return redirect('home')
#         context = {'form': form}
#         return render(request, 'users/register.html', context)
    





class Login(View):
    def get(self,request):
        context = {
            'form': LoginForm()
        }
        return render(request,'login.html',context)

    def post(self,request):
        form = LoginForm(request.POST,request = request)
        if form.is_valid():
            form.login_user()
            return render(request,'home')
        context = {
            'form':form
        }
        return render(request,'login.html',context)

