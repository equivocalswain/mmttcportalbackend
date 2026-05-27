
from django.shortcuts import render

def admin_dashboard(request):
    print(f"User: {request.user}")
    print(f"Authenticated: {request.user.is_authenticated}")
    return render(request, 'dashboard/admin_dashboard.html')

def applicant_dashboard(request):
    return render(request, 'dashboard/applicant_dashboard.html')