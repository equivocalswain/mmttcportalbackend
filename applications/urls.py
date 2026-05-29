from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:course_pk>/', views.apply_course, name='apply_course'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('upload-hod/<int:pk>/', views.upload_hod_form, name='upload_hod_form'),
]