from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def applicant_dashboard(request):
    return render(request, 'dashboard/applicant_dashboard.html')