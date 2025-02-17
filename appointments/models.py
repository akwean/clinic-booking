# clinic-booking/appointments/models.py

from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    purpose = models.TextField()
    date = models.DateField()
    time = models.TimeField()
   

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time}"