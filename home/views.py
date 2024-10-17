from django.shortcuts import render
from product.models import Category
from product.models import ProductVisit,Product
from cart.models import Cart,CartItem

# Create your views here.
def home(request):
    most_sold = Cart.cartitem_set
    # x = CartItem.cartitem_set.all()
    # print(x)
    # print(most_sold)
    # Product.objects.filter('cartitem_set')

    visits = ProductVisit.objects.filter(user=request.user)[:5]
    # print(x[0].product)
    return render(request,'home/home.html',{'visits':visits})

