from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#@login_required(login_url='login:login')
# for the restricted pages
# Create your views here.

def registerPage(request):
  if request.user.is_authenticated:
    form = CreateUserForm()

    if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, "Account was created for " + user)
        return redirect('login:login')


    context = {
      'form': form
    }
    return render(request, 'register.html', context)
    
  else:
    return redirect('homepage:index')

def loginPage(request):
  if request.user.is_authenticated:
    return redirect('homepage:index')
  else:
    context = {}
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('homepage:index')
      else:
        messages.info(request, 'Username OR password is incorrect!')
        
    return render(request, 'login.html', context)

@login_required(login_url='login:login')
def logoutUser(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('homepage:index')
  else:
    return redirect('login:login')
  
@login_required(login_url='login:login')
def profile(request):
  if request.user.is_authenticated:
    return render(request, 'profile.html')
  else:
    return redirect('login:login')