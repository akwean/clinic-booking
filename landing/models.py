from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"