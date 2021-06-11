from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from .managers import CustomUserManager


GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
    ('None','Prefer not to say'),
    ]

class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    full_name = models.CharField(max_length=100, help_text='Help people discover your account by using the name',null=True)
    email = models.EmailField(unique=True)

    # Optional fields
    bio = models.TextField(null=True, blank=True, help_text='Provide your personal information, This won\'t be a part of your public profile.')
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','full_name']

    #objects = CustomUserManager()

    def __str__(self):
        return self.username
    