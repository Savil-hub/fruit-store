from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.urls import reverse 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_auth:home')
    return render(request, 'registration/login.html', {'form': AuthenticationForm()})

def authenticate_user(request):
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
    else:
        return HttpResponseRedirect(reverse('user_auth:login'))

def show_user(request):
    print(request.user.username)
    return render(request, 'registration/user.html', {"username": request.user.username})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Make sure 'home' is a valid URL
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('user_auth:login')