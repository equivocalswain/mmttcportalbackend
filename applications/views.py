from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Application
from .forms import ApplicationForm
from courses.models import Course

def apply_course(request, course_pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    course = get_object_or_404(Course, pk=course_pk)
    
    # Check if already applied
    if Application.objects.filter(applicant=request.user, course=course).exists():
        messages.warning(request, 'You have already applied for this course!')
        return redirect('applicant_course_list')
    
    # Check if course is closed
    if course.is_closed:
        messages.error(request, 'This course is no longer accepting applications!')
        return redirect('applicant_course_list')

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.course = course
            application.status = 'pending'
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('my_applications')
    else:
        # Pre-fill form with user data
        initial = {
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'phone': request.user.phone,
            'institution': request.user.institution,
            'designation': request.user.designation,
            'state': request.user.state,
        }
        form = ApplicationForm(initial=initial)
    
    return render(request, 'applications/apply.html', {'form': form, 'course': course})


def my_applications(request):
    if not request.user.is_authenticated:
        return redirect('login')
    applications = Application.objects.filter(applicant=request.user).order_by('-submitted_at')
    return render(request, 'applications/my_applications.html', {'applications': applications})


def upload_hod_form(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    if request.method == 'POST' and request.FILES.get('hod_signed_form'):
        application.hod_signed_form = request.FILES['hod_signed_form']
        application.save()
        messages.success(request, 'HoD signed form uploaded successfully!')
        return redirect('my_applications')
    return render(request, 'applications/upload_hod.html', {'application': application})