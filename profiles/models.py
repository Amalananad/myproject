from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
from django.db import models

# Create your models here.
