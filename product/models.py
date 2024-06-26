from django.db import models

# Create your models here.
    


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    slug = models.SlugField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    main_picture = models.ImageField(upload_to='product', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

        
class ProductGallery(models.Model):
    picture = models.ImageField(upload_to='product_other_picture', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)