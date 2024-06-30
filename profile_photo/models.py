from django.db import models
# Create your models here.
class user_profile(models.Model):
    user_profile=models.ImageField(upload_to='profile_picture',default='./static/img/download.jpeg')
