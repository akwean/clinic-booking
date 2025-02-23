from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    # Hidden date field
    date = forms.DateField(
        widget=forms.HiddenInput(
            attrs={
                'id': 'selected_date',
                'required': True,
            }
        ),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Appointment
        fields = [
            'first_name', 'last_name', 'course', 'block', 'year', 'purpose', 
            'time', 'date', 'types_of_client', 'parent_guardian', 'contact_no', 
            'home_address', 'additional_notes'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'block': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'types_of_client': forms.Select(attrs={'class': 'form-control'}),
            'parent_guardian': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'home_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }