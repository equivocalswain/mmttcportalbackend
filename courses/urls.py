from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('toggle-visibility/<int:pk>/', views.course_toggle_visibility, name='course_toggle_visibility'),
    path('toggle-closed/<int:pk>/', views.course_toggle_closed, name='course_toggle_closed'),
    path('available/', views.applicant_course_list, name='applicant_course_list'),    # new
    path('detail/<int:pk>/', views.course_detail, name='course_detail'),              # new
]