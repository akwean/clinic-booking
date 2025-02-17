from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    COURSE_CHOICES = [
        ('course1', 'Course 1'),
        ('course2', 'Course 2'),
        # add other choices...
    ]
    BLOCK_CHOICES = [
        ('block1', 'Block 1'),
        ('block2', 'Block 2'),
        # add other choices...
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    block = models.CharField(max_length=10, choices=BLOCK_CHOICES)
    # other fields..

    def __str__(self):
        return self.user.username

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
def save_user_profile(sender, instance, **kwargs):
  

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
