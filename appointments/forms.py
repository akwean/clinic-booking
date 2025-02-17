# clinic-booking/appointments/forms.py

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name' , 'course', 'block', 'year', 'purpose','date', 'time']