from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

GENDER=(
    ('male', 'MALE'),('female', 'FEMALE')
)
CATEGORIES=(
    ('full_marathon','Full Marathon'),('half_marathon','Half Marathon'),('10K_marathon', '10K MARATHON')
)

# Create your models here.
class Participant(AbstractUser):
    categories=models.CharField(max_length=20, choices= CATEGORIES, default= 'full_marathon')
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    email_address = models.EmailField(unique=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    emergency_contact_number = models.CharField(max_length=20)
    relationship = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.username} form has been created "




