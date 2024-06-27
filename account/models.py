from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=13)
    meli_code = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    address = models.TextField(null=True,blank=True)
    # verification code
    v_code = models.CharField(max_length=5,default=False,null=True,blank=True)