from django.shortcuts import render
from django.http import JsonResponse
from .models import Cart, CartItem
from product.models import Product
# Create your views here.
def add_to_cart(request,product_id):
    user_cart = Cart.objects.filter(user=request.user,is_paid=False).first()
    if user_cart == None:
        print('new cart was created...')
        new_cart = Cart(user=request.user)
        new_cart.save()
        user_product = Product.objects.get(id=product_id)
        new_cart_item = CartItem(cart=new_cart,product=user_product)
        new_cart_item.save()
    else:
        cart_itme_exists = user_cart.cartitem_set.all().filter(product_id=product_id).exists()
        if cart_itme_exists == True:
            print('cart item amount increses ...')
            user_cart_item = CartItem.objects.get(user=request.user,product_id=product_id)
            user_cart_item.amount += 1
            user_cart_item.save()
        else:
            print('new cart time was created ...')
            user_product = Product.objects.get(id=product_id)
            new_cart_item = CartItem(cart=user_cart,product=user_product)
            new_cart_item.save()

    # print(user_cart)
    print('*'*90)
    # print(product_id)
    # print('*'*90)
    return JsonResponse({'status':'ok', 'message':'soma kheyli khobid'})


def cart(request):
    user_cart = Cart.objects.filter(user=request.user ,is_paid = False).first()
    cart_items = user_cart.cartitem_set.all()
    return render(request,'cart/cart.html',{'cart_items':cart_items,'user_cart':user_cart})



def plus_cart_item(request, cartitem_id):
    user_cart_item = CartItem.objects.get(id=cartitem_id)
    user_cart_item.amount += 1
    user_cart_item.save()
    # print(cartitem_id)
    user_cart = Cart.objects.filter(user=request.user ,is_paid = False).first()
    
    return JsonResponse({'status':'ok', 'amount':user_cart_item.amount,'total_price':user_cart.get_total_price()})