# clinic-booking/appointments/models.py

from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    

    YEAR_CHOICES = [
        ('1st', 'First Year'),
        ('2nd', 'Second Year'),
        ('3rd', 'Third Year'),
        ('4th', 'Fourth Year'),
    ]
    
    PURPOSE_CHOICES = [
        ('medical_check', 'Medical Check-up'),
        ('consultation', 'Consultation'),
        ('emergency', 'Emergency'),
        ('follow_up', 'Follow-up Check'),
        ('medicine', 'Medicine Request'),
        ('certificate', 'Medical Certificate'),
        ('others', 'Others'),
    ]
    
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    year = models.CharField(max_length=3, choices=YEAR_CHOICES)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    additional_notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time}"