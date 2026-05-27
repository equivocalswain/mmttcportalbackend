from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'applicant'
            user.save()
            # authenticate then login
            authenticated_user = authenticate(
                request,
                username=user.username,
                password=request.POST['password1']
            )
            if authenticated_user:
                login(request, authenticated_user)
            return redirect('applicant_dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}")
        print(f"Password: {password}")
        
        # Check if user exists
        from accounts.models import CustomUser
        try:
            u = CustomUser.objects.get(username=username)
            print(f"User found in DB: {u}")
            print(f"Password check: {u.check_password(password)}")
        except:
            print("User NOT found in DB")
        
        user = authenticate(request, username=username, password=password)
        print(f"authenticate() returned: {user}")
        
        if user is not None:
            login(request, user)
            if user.is_superuser or getattr(user, 'role', None) == 'admin':
                return redirect('admin_dashboard')
            return redirect('applicant_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')