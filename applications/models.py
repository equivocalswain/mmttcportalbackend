from django.db import models
from accounts.models import CustomUser
from courses.models import Course

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    TITLE_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Dr.', 'Dr.'),
        ('Prof.', 'Prof.'),
    ]
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('EWS', 'EWS'),
    ]
    FACULTY_CHOICES = [
        ('Faculty', 'Faculty'),
        ('Researcher/Non-Teaching', 'Researcher/Non-Teaching'),
    ]
    QUALIFICATION_CHOICES = [
        ('Graduate', 'Graduate'),
        ('Post Graduate', 'Post Graduate'),
        ('M.Phil', 'M.Phil'),
        ('Ph.D', 'Ph.D'),
        ('Post Doctoral', 'Post Doctoral'),
    ]
    COURSE_TYPE_CHOICES = [
    ('OC', 'OC - Orientation Courses'),
    ('RC-I', 'RC-I - Refresher Courses'),
    ('SC', 'SC - Short Term Courses'),
    ('NEP', 'NEP'),
]

    # Core
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    course_type = models.CharField(max_length=10, choices=COURSE_TYPE_CHOICES, blank=True)

    # Personal Details
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    full_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    pwd = models.BooleanField(default=False)
    aadhaar = models.CharField(max_length=12)
    photograph = models.ImageField(upload_to='applications/photos/', blank=True, null=True)
    dob = models.DateField()
    faculty_type = models.CharField(max_length=30, choices=FACULTY_CHOICES)

    # Contact Details
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    alternate_mobile = models.CharField(max_length=10, blank=True)
    institute_address = models.CharField(max_length=100)
    institute_state = models.CharField(max_length=100)
    institute_pincode = models.CharField(max_length=6)
    same_as_institute = models.BooleanField(default=False)
    mailing_address = models.CharField(max_length=100, blank=True)
    mailing_state = models.CharField(max_length=100, blank=True)
    mailing_pincode = models.CharField(max_length=6, blank=True)

    # Academic
    highest_qualification = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES)

    # Previous Courses
    prev_course1 = models.CharField(max_length=100, blank=True)
    prev_course1_year = models.CharField(max_length=10, blank=True)
    prev_course1_center = models.CharField(max_length=50, blank=True)
    prev_course2 = models.CharField(max_length=100, blank=True)
    prev_course2_year = models.CharField(max_length=10, blank=True)
    prev_course2_center = models.CharField(max_length=50, blank=True)

    # Accommodation
    accommodation = models.BooleanField(default=False)

    # Documents
    original_form = models.FileField(upload_to='applications/forms/', blank=True, null=True)
    hod_signed_form = models.FileField(upload_to='applications/hod_signed/', blank=True, null=True)

    # Admin
    admin_remarks = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.course.title}"

    class Meta:
        unique_together = ['applicant', 'course']