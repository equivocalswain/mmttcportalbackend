from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser
from courses.models import Course

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Personal details
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    institution = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    # Documents
    original_form = models.FileField(upload_to='applications/forms/', blank=True, null=True)
    hod_signed_form = models.FileField(upload_to='applications/hod_signed/', blank=True, null=True)
    
    admin_remarks = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.course.title}"

    class Meta:
        unique_together = ['applicant', 'course']  # one application per course