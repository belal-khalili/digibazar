from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
from .models import Category

# Create your views here.
def category_view(request,catName):
    cat_id = Category.objects.get(link=catName)
    data = Product.objects.filter(category=cat_id.id)
    categories = Category.objects.all()
    cat_name = cat_id.title

    return render(request,'category/category.html',{'products':data,'categories':categories,'cat_name':cat_name})