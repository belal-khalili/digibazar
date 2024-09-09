from django.db import models
from account.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Publisher(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.title

class veblog(models.Model):
    title = models.CharField(max_length=100)
    body=RichTextField(blank=type,null=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    main_text = models.TextField()
    img = models.ImageField(upload_to='blog.image', null=True, blank=True)
    date = models.DateField()
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.title