from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from appointments.models import Appointment

class Command(BaseCommand):
    help = 'Creates nurse group with appropriate permissions'

    def handle(self, *args, **options):
        nurse_group, created = Group.objects.get_or_create(name='Nurses')
        
        # Get appointment content type
        appointment_content_type = ContentType.objects.get_for_model(Appointment)
        
        # Define permissions nurses should have
        permissions = Permission.objects.filter(
            content_type=appointment_content_type,
            codename__in=['change_appointment', 'view_appointment']
        )
        
        # Add permissions to group
        nurse_group.permissions.set(permissions)
        
        self.stdout.write(self.style.SUCCESS('Successfully created nurse group'))