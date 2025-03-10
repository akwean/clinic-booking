# clinic-booking/appointments/models.py

from django.db import models
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils import timezone

class Appointment(models.Model):
    # Status choices for the appointment
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Year choices for the appointment
    YEAR_CHOICES = [
        ('1st', 'First Year'),
        ('2nd', 'Second Year'),
        ('3rd', 'Third Year'),
        ('4th', 'Fourth Year'),
    ]
    
    # Purpose choices for the appointment
    PURPOSE_CHOICES = [
        ('medical', 'Medical (consultation & treatment)'),
        ('physical_examination', 'Physical examination (e.g., athletic activities, OJT/internship, extra-curricular, scholarship)'),
        ('dental', 'Dental consultation & treatment'),
        ('vaccination', 'Vaccination (Flu & Pneumonia) done annually (free)'),
    ]
    
    # Client type choices for the appointment Remove for now
    '''CLIENT_CHOICES = [
        ('student', 'Student'),
        ('personnel', 'Personnel'),
        ('non_bu_personnel', 'Non-BU Personnel (e.g., part-timers)'),
        ('others', 'Others (guests)'),
    ]'''
    
    # Time choices for the appointment
    TIME_CHOICES = [
        ('09:00', '9:00 AM'),
        ('09:30', '9:30 AM'),
        ('10:00', '10:00 AM'),
        ('10:30', '10:30 AM'),
        ('11:00', '11:00 AM'),
        ('11:30', '11:30 AM'),
        ('13:00', '1:00 PM'),
        ('13:30', '1:30 PM'),
        ('14:00', '2:00 PM'),
        ('14:30', '2:30 PM'),
        ('15:00', '3:00 PM'),
        ('15:30', '3:30 PM'),
        ('16:00', '4:00 PM'),
    ]

    # Fields for the appointment model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    year = models.CharField(max_length=3, choices=YEAR_CHOICES)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    #types_of_client = models.CharField(max_length=20, choices=CLIENT_CHOICES, default='student') Remove for now
    parent_guardian = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    home_address = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    additional_notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(default=timezone.now)

    # Save method to handle notifications
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_status = None
        if not is_new:
            old_status = Appointment.objects.get(pk=self.pk).status

        super().save(*args, **kwargs)

        channel_layer = get_channel_layer()
        if channel_layer is None:
            print("Channel layer is None")
        else:
            async_to_sync(channel_layer.group_send)(
                "appointments",
                {
                    "type": "appointment_message",
                    "message": self.to_dict()
                }
            )

            if not is_new and old_status != self.status:
                async_to_sync(channel_layer.group_send)(
                    f"appointment_{self.user.id}",
                    {
                        "type": "appointment_status_update",
                        "message": self.to_dict()
                    }
                )

    # Convert appointment to dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.strftime('%Y-%m-%d'),
            "time": self.time,
            "purpose": self.get_purpose_display(),
            "status": self.get_status_display(),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "course": self.course,
            "block": self.block,
            "year": self.year,
            "additional_notes": self.additional_notes or "None",
            #"types_of_client": self.get_types_of_client_display(),
            "parent_guardian": self.parent_guardian,
            "contact_no": self.contact_no,
            "home_address": self.home_address,
        }

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time}"