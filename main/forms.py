from django import forms
from .models import Appointment


class NewAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['hospital', 'when', 'patient_code',
                  'first_name', 'last_name', 'father_name', 'mother_name',
                  'insurance_id', 'gender', 'birthday',
                  'home_address', 'mobile_number', 'home_number', 'work_number',
                  'allergies', 'chronic_diseases', 'other_medical_info']



