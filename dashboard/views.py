from django.shortcuts import render
from courses.models import Course
from applications.models import Application

def admin_dashboard(request):
    # Application statistics
    total_applications = Application.objects.count()
    pending = Application.objects.filter(status='pending').count()
    approved = Application.objects.filter(status='approved').count()
    rejected = Application.objects.filter(status='rejected').count()

    # Course statistics
    total_courses = Course.objects.count()
    open_courses = Course.objects.filter(is_visible=True, is_closed=False).count()

    # Course wise data
    courses = Course.objects.all()

    context = {
        'total_applications': total_applications,
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
        'total_courses': total_courses,
        'open_courses': open_courses,
        'courses': courses,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

def applicant_dashboard(request):
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')
    
    from applications.models import Application
    my_applications = Application.objects.filter(applicant=request.user)
    total = my_applications.count()
    pending = my_applications.filter(status='pending').count()
    approved = my_applications.filter(status='approved').count()
    rejected = my_applications.filter(status='rejected').count()

    context = {
        'total': total,
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
    }
    return render(request, 'dashboard/applicant_dashboard.html', context)