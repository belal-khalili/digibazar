from django.shortcuts import render
from .models import Product,ProductVisit
from utils.ip_service import get_client_ip
from django.db.models import Q
import json
# Create your views here.
def products(request):
    data = Product.objects.filter(is_active=True).order_by('-id')
    return render(request,'product/products.html',{'products':data})


def single_product(request,slug):
    data = Product.objects.get(slug=slug)
    if not request.user.is_authenticated:
        visit = ProductVisit.objects.filter(ip_address=get_client_ip(request),product=data).exists()
        if not visit:
            new_visit = ProductVisit(ip_address=get_client_ip(request),product=data)
            new_visit.save()
    else:
        visit = ProductVisit.objects.filter(ip_address=get_client_ip(request),user=request.user,product=data).exists()
        if not visit:
            new_visit = ProductVisit(user=request.user,product=data,ip_address=get_client_ip(request))
            new_visit.save()

    # TODO: this needs tkinking about what to do with multiple categorys 
    # related_products = Product.objects.filter(category)

    # print(get_client_ip(request))
    # print(request.META)
        
    return render(request, 'product/single_product.html',{'product':data})


def product_filter(request):
    return render(request, 'product/product_filter.html')


def filter_result(request):
    data = json.loads(request.body)
    print(type(data['filter_val_max']))
    # filter_range
    min_price = data['filter_val_min']
    max_price = data['filter_val_max']
    products = Product.objects.filter(price__lte=max_price,price__gte=min_price)
    return render(request,'product/filter_result.html',{'products': products})