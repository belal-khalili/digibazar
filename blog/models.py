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

class Blog(models.Model):
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
    

class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blogcomment_set')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_blogcomment_set')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    like = models.ManyToManyField(User,related_name='like_blogcomment_set',blank=True)
    dislike = models.ManyToManyField(User,related_name='dislike_blogcomment_set',blank=True)
    admin_verify = models.BooleanField(default=False, choices={True:'تایید', False:'رد'})
    parent = models.ForeignKey('BlogComment', null=True, blank=True, related_name='blogcomment_blogcomment_set', on_delete=models.CASCADE)

    def show_likes(self):
        return self.like.all().count()
    
    def show_dislikes(self):
        return self.dislike.all().count()