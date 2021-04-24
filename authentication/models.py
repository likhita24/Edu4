from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    college = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username
