from django.urls import path
from . import views

urlpatterns = [
    path('generate/<int:application_pk>/', views.generate_certificate, name='generate_certificate'),
    path('download/<int:pk>/', views.download_certificate, name='download_certificate'),
    path('my-certificates/', views.my_certificates, name='my_certificates'),
]