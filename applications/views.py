from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Application
from .forms import ApplicationForm
from courses.models import Course
from django.core.mail import send_mail
from django.conf import settings

def apply_course(request, course_pk):
    if not request.user.is_authenticated:
        return redirect('login')

    course = get_object_or_404(Course, pk=course_pk)

    if Application.objects.filter(applicant=request.user, course=course).exists():
        messages.warning(request, 'You have already applied for this course!')
        return redirect('applicant_course_list')

    if course.is_closed:
        messages.error(request, 'This course is no longer accepting applications!')
        return redirect('applicant_course_list')

    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
        'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
        'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
        'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
        'Andaman and Nicobar Islands', 'Chandigarh', 'Delhi',
        'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry',
        'Dadra and Nagar Haveli and Daman and Diu'
    ]

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.course = course
            application.status = 'pending'
            application.course_type = request.POST.get('course_type', '')
            # Handle pwd and accommodation boolean
            application.pwd = request.POST.get('pwd') == 'True'
            application.accommodation = request.POST.get('accommodation') == 'True'
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('my_applications')
        else:
            print(form.errors)
    else:
        form = ApplicationForm()

    return render(request, 'applications/apply.html', {
        'form': form,
        'course': course,
        'states': states
    })

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


def admin_application_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    applications = Application.objects.all().order_by('-submitted_at')
    status = request.GET.get('status')
    if status in ['pending', 'approved', 'rejected']:
        applications = applications.filter(status=status)

    return render(request, 'applications/admin_application_list.html', {
        'applications': applications,
        'current_status': status
    })


def admin_application_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'applications/admin_application_detail.html', {'application': application})


def approve_application(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        application.status = 'approved'
        application.admin_remarks = request.POST.get('remarks', '')
        application.save()
        course = application.course
        course.seats_filled += 1
        course.save()
        messages.success(request, f'{application.full_name} has been approved!')
        return redirect('admin_application_list')
    return render(request, 'applications/admin_application_detail.html', {'application': application})


def reject_application(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        application.status = 'rejected'
        application.admin_remarks = request.POST.get('remarks', '')
        application.save()
        messages.success(request, f'{application.full_name} has been rejected.')
        return redirect('admin_application_list')
    return render(request, 'applications/admin_application_detail.html', {'application': application})
def print_application(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    return render(request, 'applications/print_application.html', {'application': application})