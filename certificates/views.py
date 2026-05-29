from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from applications.models import Application
from .models import Certificate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import uuid
import os
from django.conf import settings


def generate_certificate_pdf(certificate):
    # File path
    filename = f"certificate_{certificate.certificate_id}.pdf"
    filepath = os.path.join(settings.MEDIA_ROOT, 'certificates', filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Create PDF
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    # Background border
    c.setStrokeColor(colors.HexColor('#1a3a5c'))
    c.setLineWidth(4)
    c.rect(30, 30, width - 60, height - 60)
    c.setLineWidth(2)
    c.rect(40, 40, width - 80, height - 80)

    # Title
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(colors.HexColor('#1a3a5c'))
    c.drawCentredString(width / 2, height - 150, "CERTIFICATE")

    c.setFont("Helvetica", 20)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawCentredString(width / 2, height - 185, "OF PARTICIPATION")

    # Divider
    c.setStrokeColor(colors.HexColor('#1a3a5c'))
    c.setLineWidth(1)
    c.line(100, height - 200, width - 100, height - 200)

    # Body text
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 240, "This is to certify that")

    # Name
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(colors.HexColor('#1a3a5c'))
    c.drawCentredString(width / 2, height - 290, certificate.application.full_name)

    # Line under name
    c.setStrokeColor(colors.HexColor('#1a3a5c'))
    c.line(150, height - 300, width - 150, height - 300)

    # Institution
    c.setFont("Helvetica", 13)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 325,
        f"{certificate.application.designation}, {certificate.application.institution}")

    # Course text
    c.drawCentredString(width / 2, height - 360, "has successfully participated in")

    # Course name
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.HexColor('#1a3a5c'))
    c.drawCentredString(width / 2, height - 395, certificate.application.course.title)

    # Duration
    c.setFont("Helvetica", 13)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 425,
        f"Duration: {certificate.application.course.duration}")

    # Dates
    c.drawCentredString(width / 2, height - 450,
        f"From {certificate.application.course.start_date} to {certificate.application.course.end_date}")

    # Organized by
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 490,
        "Organized by Malaviya Mission Teacher Training Centre (MMTTC)")

    # Divider
    c.line(100, height - 520, width - 100, height - 520)

    # Certificate ID and date
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.grey)
    c.drawString(60, 80, f"Certificate ID: {certificate.certificate_id}")
    c.drawString(60, 65, f"Issued on: {certificate.issued_on}")

    c.save()
    return f"certificates/{filename}"


def generate_certificate(request, application_pk):
    if not request.user.is_authenticated:
        return redirect('login')

    application = get_object_or_404(Application, pk=application_pk)

    # Only for approved applications
    if application.status != 'approved':
        messages.error(request, 'Certificate can only be generated for approved applications!')
        return redirect('admin_application_list')

    # Check if already exists
    if Certificate.objects.filter(application=application).exists():
        messages.warning(request, 'Certificate already generated!')
        return redirect('admin_application_list')

    # Create certificate
    certificate = Certificate.objects.create(application=application)
    pdf_path = generate_certificate_pdf(certificate)
    certificate.pdf_file = pdf_path
    certificate.save()

    messages.success(request, f'Certificate generated for {application.full_name}!')
    return redirect('admin_application_list')


def download_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    filepath = os.path.join(settings.MEDIA_ROOT, str(certificate.pdf_file))

    with open(filepath, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="certificate_{certificate.application.full_name}.pdf"'
        return response


def my_certificates(request):
    if not request.user.is_authenticated:
        return redirect('login')
    certificates = Certificate.objects.filter(
        application__applicant=request.user,
        application__status='approved'
    )
    return render(request, 'certificates/my_certificates.html', {'certificates': certificates})