from django.contrib import admin
from .models import Product,ProductGallery,Category,ProductVisit
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductGallery)
admin.site.register(ProductVisit)

