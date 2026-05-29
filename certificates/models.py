from django.db import models
from applications.models import Application
import uuid

class Certificate(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    certificate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    issued_on = models.DateField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"Certificate - {self.application.full_name}"