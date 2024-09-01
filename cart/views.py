from django.shortcuts import render
from django.http import JsonResponse
from .models import Cart
# Create your views here.
def add_to_cart(request,product_id):
    print('*'*90)
    print(product_id)
    print('*'*90)
    return JsonResponse({'status':'ok', 'message':'soma kheyli khobid'})


def cart(request):
    user_cart = Cart.objects.filter(user=request.user ,is_paid = False).first()
    cart_items = user_cart.cartitem_set.all()
    return render(request,'cart/cart.html',{'cart_items':cart_items,'user_cart':user_cart})