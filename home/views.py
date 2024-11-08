from django.shortcuts import render
from product.models import Category
from product.models import ProductVisit,Product
from cart.models import Cart,CartItem
from product.models import Product
from django.db.models import Avg,Sum,Min,Count

# Create your views here.
def home(request):
    # all_p = Product.objects.all().aggregate(min_price=Count('price'))
    # print(all_p)
    most_sold_products = Product.objects.filter(cartitem__cart__is_paid=True).annotate(quantity=Sum('cartitem__amount')).order_by('-quantity')[:10]
    visits = ProductVisit.objects.filter(user=request.user)[:5]
    # print(x[0].product)
    return render(request,'home/home.html',{'visits':visits, 'most_sold_products':most_sold_products})

