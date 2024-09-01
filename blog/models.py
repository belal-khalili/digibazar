from django.db import models
from account.models import User
# Create your models here.
class veblog(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    main_text = models.TextField()
    img = models.ImageField(upload_to='blog.image', null=True, blank=True)
    date = models.DateField()

    def __str__(self) -> str:
        return self.title