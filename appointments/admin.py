from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'date', 'time', 'course', 'block', 'purpose')
    list_filter = ('date', 'course', 'block', 'purpose')
    search_fields = ('user__username', 'first_name', 'last_name')
    readonly_fields = ('user',)
    ordering = ('-date', 'time')