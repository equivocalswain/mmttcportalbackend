from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:course_pk>/', views.apply_course, name='apply_course'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('upload-hod/<int:pk>/', views.upload_hod_form, name='upload_hod_form'),
    
    # Admin URLs
    path('admin/list/', views.admin_application_list, name='admin_application_list'),
    path('admin/detail/<int:pk>/', views.admin_application_detail, name='admin_application_detail'),
    path('admin/approve/<int:pk>/', views.approve_application, name='approve_application'),
    path('admin/reject/<int:pk>/', views.reject_application, name='reject_application'),
]