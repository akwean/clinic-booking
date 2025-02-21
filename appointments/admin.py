from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    change_list_template = 'admin/appointments/appointment/change_list.html'  # Use custom template

    list_display = (
        'user', 
        'first_name', 
        'last_name', 
        'date', 
        'time', 
        'course', 
        'block', 
        'year',
        'purpose',
        'status_badge',  # Changed from status_display
        'additional_notes'
    )
    
    list_filter = ('date', 'course', 'block', 'purpose', 'status', 'year')
    search_fields = ('user__username', 'first_name', 'last_name', 'additional_notes')
    readonly_fields = ('user', 'first_name', 'last_name', 'course', 'block', 'year', 
                      'purpose', 'date', 'time', 'additional_notes')
    actions = ['approve_appointments', 'reject_appointments', 'complete_appointments']

    def status_badge(self, obj):
        status_colors = {
            'pending': '#ffc107',
            'approved': '#28a745',
            'rejected': '#dc3545',
            'completed': '#17a2b8'
        }
        
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; '
            'border-radius: 4px;">{}</span>',
            status_colors.get(obj.status, '#6c757d'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def approve_appointments(self, request, queryset):
        self.update_status(request, queryset, 'approved')
    approve_appointments.short_description = "Mark selected appointments as approved"

    def reject_appointments(self, request, queryset):
        self.update_status(request, queryset, 'rejected')
    reject_appointments.short_description = "Mark selected appointments as rejected"

    def complete_appointments(self, request, queryset):
        self.update_status(request, queryset, 'completed')
    complete_appointments.short_description = "Mark selected appointments as completed"

    def update_status(self, request, queryset, status):
        channel_layer = get_channel_layer()
        for appointment in queryset:
            appointment.status = status
            appointment.save()
            async_to_sync(channel_layer.group_send)(
                "appointments",
                {
                    "type": "appointment_message",
                    "message": appointment.to_dict()
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"appointment_{appointment.user.id}",
                {
                    "type": "appointment_status_update",
                    "message": appointment.to_dict()
                }
            )
        self.message_user(request, f"Successfully marked {queryset.count()} appointments as {status}.", messages.SUCCESS)