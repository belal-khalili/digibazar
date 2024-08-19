from django.db import models
from account.models import User
# Create your models here.

class veblog(models.model):
    title=models.CharField()
    publisher=models.CharField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    main_text=models.TextField()
    img=models.ImageField(upload_to='blog.image')
    date=models.DateField()
