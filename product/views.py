from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    data = Product.objects.all().order_by('-id')[:3]
    return render(request,'product/products.html',{'products':data})


def single_product(request,slug):
    data = Product.objects.get(slug=slug)
    print(data.productgallery_set.all())
    return render(request, 'product/single_product.html',{'product':data})