from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landing_page')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing_page')
        
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Debug
            user = form.save()
            print("User created:", user.username)  # Debug
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('landing_page')
        else:
            print("Form is not valid:", form.errors)  # Debug
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
