from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    COURSE_CHOICES = [
    ('BEED', 'Bachelor in Elementary Education'),
    ('BSED', 'Bachelor of Secondary Education'),
    ('BSCS', 'Bachelor of Science in Computer Science'),
    ('BSIS', 'Bachelor of Science in Information System'),
    ('BSIT', 'Bachelor of Science in Information Technology'),
    ('BSIT Anim', 'Bachelor of Science in Information Technology with Specialization in Animation'),
    ('BSCpE', 'Bachelor of Science in Computer Engineering'),
    ('BSEE', 'Bachelor of Science in Electronics Engineering'),
    ('BSN', 'Bachelor of Science in Nursing'),
    ('BSAT', 'Bachelor of Science in Automotive Technology'),
    ('BSET', 'Bachelor of Science in Electrical Technology'),
    ('BSEnt', 'Bachelor of Science in Entrepreneurship'),
    ('BSEt', 'Bachelor of Science in Electronics Technology'),
    ('BSFT', 'Bachelor of Science in Food Technology'),
    ('BSMT', 'Bachelor of Science in Mechanical Technology'),
]

    BLOCK_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        # add other choices...
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    block = models.CharField(max_length=10, choices=BLOCK_CHOICES)
    # other fields..

    def __str__(self):
        return self.user.username


