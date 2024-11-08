from django.contrib import admin
from .models import Product,ProductGallery,Category,ProductVisit
# Register your models here.
@admin.action(description="فعال کردن همه انتخاب شده ها")
def make_published(modeladmin, request, queryset):
    queryset.update(is_active=True)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag','title','price']
    actions = [make_published]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(ProductVisit)

