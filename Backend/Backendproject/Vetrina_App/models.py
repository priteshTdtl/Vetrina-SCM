from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    profile_picture = models.URLField(blank=True, null=True)
    account_status = models.CharField(max_length=20, default='active')
    created_by=models.CharField(max_length=20, default='user')
    last_login = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
