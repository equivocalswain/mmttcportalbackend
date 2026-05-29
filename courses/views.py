from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from accounts.models import CustomUser

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            user = CustomUser.objects.get(pk=request.user.pk)
            course.created_by = user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Create Course'})

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Edit Course'})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

def course_toggle_visibility(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.is_visible = not course.is_visible
    course.save()
    return redirect('course_list')

def course_toggle_closed(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.is_closed = not course.is_closed
    course.save()
    return redirect('course_list')
def applicant_course_list(request):
    courses = Course.objects.filter(is_visible=True, is_closed=False)
    return render(request, 'courses/applicant_course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})