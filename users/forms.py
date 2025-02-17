# clinic-booking/users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    course = forms.ChoiceField(choices=Profile.COURSE_CHOICES, required=True, help_text='Required')
    block = forms.ChoiceField(choices=Profile.BLOCK_CHOICES, required=True, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'course', 'block', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            print("Profile created:", created)  # Debug
            profile.course = self.cleaned_data['course']
            profile.block = self.cleaned_data['block']
            print("Course:", profile.course)  # Debug
            print("Block:", profile.block)  # Debug
            profile.save()
        return user
