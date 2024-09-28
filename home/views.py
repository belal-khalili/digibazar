from django.shortcuts import render
from product.models import Category
# Create your views here.
def home(request):
    return render(request,'home/home.html')