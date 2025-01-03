from django.db import models
from category.models import Category
from account.models import User
from django.utils.html import format_html
# Create your models here.
    

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    slug = models.SlugField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    main_picture = models.ImageField(upload_to='product', null=True, blank=True)
    category = models.ManyToManyField(Category)
    # sold = models.IntegerField()

    def __str__(self) -> str:
        return self.title


    def image_tag(self):
        return format_html(f"<img width=80 height=60 src='{self.main_picture.url}'>")
     

class ProductVisit(models.Model):
    user = models.ForeignKey(User,null=True , on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=15)
    # count = models.IntegerField(default=0)
    # timestamp = models.DateTimeField(auto_now_add=True)

        
class ProductGallery(models.Model):
    picture = models.ImageField(upload_to='product_other_picture', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)