from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or getattr(request.user, 'role', None) == 'admin':
            return redirect('admin_dashboard')
        return redirect('applicant_dashboard')
    return redirect('login')

urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('courses/', include('courses.urls')),
    path('applications/', include('applications.urls')),
    path('certificates/', include('certificates.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)