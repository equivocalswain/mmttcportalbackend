from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    APPLICANT = 'applicant'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (APPLICANT, 'Applicant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=APPLICANT)
    institution = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=100, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )

    def is_admin_user(self):
        return self.role == self.ADMIN