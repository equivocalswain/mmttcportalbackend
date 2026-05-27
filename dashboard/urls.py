from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('applicant-dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
]