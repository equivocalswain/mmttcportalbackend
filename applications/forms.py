from django import forms
from .models import Application

STATES = [
    ('', 'Select State'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
]

class ApplicationForm(forms.ModelForm):
    institute_state = forms.ChoiceField(choices=STATES)
    mailing_state = forms.ChoiceField(choices=STATES, required=False)

    class Meta:
        model = Application
        fields = [
            'title', 'full_name', 'category', 'pwd',
            'aadhaar', 'photograph', 'dob', 'faculty_type',
            'email', 'mobile', 'alternate_mobile',
            'institute_address', 'institute_state', 'institute_pincode',
            'same_as_institute', 'mailing_address', 'mailing_state', 'mailing_pincode',
            'highest_qualification',
            'prev_course1', 'prev_course1_year', 'prev_course1_center',
            'prev_course2', 'prev_course2_year', 'prev_course2_center',
            'accommodation', 'original_form',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'faculty_type': forms.Select(attrs={'class': 'form-select'}),
            'highest_qualification': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
            'aadhaar': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '12'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'alternate_mobile': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'institute_address': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
            'institute_pincode': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '6'}),
            'mailing_address': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
            'mailing_pincode': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '6'}),
            'prev_course1': forms.TextInput(attrs={'class': 'form-control'}),
            'prev_course1_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YYYY'}),
            'prev_course1_center': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}),
            'prev_course2': forms.TextInput(attrs={'class': 'form-control'}),
            'prev_course2_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YYYY'}),
            'prev_course2_center': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}),
        }