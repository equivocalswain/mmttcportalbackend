from django.db import models
from accounts.models import CustomUser

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.TextField()
    duration = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_seats = models.IntegerField()
    seats_filled = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    is_closed = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def seats_available(self):
        return self.total_seats - self.seats_filled

    def __str__(self):
        return self.title