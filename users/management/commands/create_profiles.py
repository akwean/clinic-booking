from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile

class Command(BaseCommand):
    help = 'Create missing profiles for users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            # Set default values for course and block
            course = 'course1'  # You can change this to a default value or fetch from user data if available
            block = 'block1'    # You can change this to a default value or fetch from user data if available
            Profile.objects.create(user=user, course=course, block=block)
            self.stdout.write(self.style.SUCCESS(f'Created profile for user {user.username} with course {course} and block {block}'))