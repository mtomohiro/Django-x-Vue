from django.forms import ModelForm
from dq.models import Appointment, Patient

class AppointmentForm(ModelForm):
    """予約のフォーム"""
    class Meta:
        model = Appointment
        fields = ('bookDateTime','patient',)

class PatientForm(ModelForm):
    """患者のフォーム"""
    class Meta:
        model = Patient
        fields = ('name','birth',)