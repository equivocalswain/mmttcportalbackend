from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import RegisterForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'applicant'
            user.save()
            login(request, user)
            return redirect('applicant_dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                if user.is_superuser or user.role == 'admin':
                    return redirect('admin_dashboard')
                return redirect('applicant_dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')