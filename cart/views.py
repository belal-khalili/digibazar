from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import Cart, CartItem
from product.models import Product
from django.utils import timezone
from django.conf import settings
import requests
import json

ZP_API_REQUEST = f"https://{settings.SANDBOX}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{settings.SANDBOX}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{settings.SANDBOX}.zarinpal.com/pg/StartPay/"


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
    return JsonResponse({'status':'ok', 'message':'soma kheyli khobid'})


def cart(request):
    user_cart = Cart.objects.filter(user=request.user ,is_paid = False).first()
    cart_items = user_cart.cartitem_set.all()
    return render(request,'cart/cart.html',{'cart_items':cart_items,'user_cart':user_cart})



def plus_cart_item(request, cartitem_id):
    user_cart_item = CartItem.objects.get(id=cartitem_id)
    user_cart_item.amount += 1
    user_cart_item.save()
    user_cart = Cart.objects.filter(user=request.user ,is_paid = False).first()
    
    return JsonResponse({'status':'ok', 'amount':user_cart_item.amount,'total_price':user_cart.get_total_price()})


def negative_cart_item(request, cartitem_id):
    user_cart_item = CartItem.objects.get(id=cartitem_id)
    user_cart_item.amount -= 1
    user_cart_item.save()
    user_cart = Cart.objects.filter(user=request.user ,is_paid = False).first()
    
    return JsonResponse({'status':'ok', 'amount':user_cart_item.amount,'total_price':user_cart.get_total_price()})



def cart_payment(request):
    user_cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    amount = user_cart.get_total_price()  # Required
    description = "فروشگاه اینترنتی دیجی بازار"  # Required
    phone = request.user.phone  # Optional
    CallbackURL = 'http://127.0.0.1:8000/cart/cart_payment_verify/'  # Required

    
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return redirect(ZP_API_STARTPAY+str(response['Authority']))
            else:
                return HttpResponse('پرداخت با شکست مواجه شد')
        return response
    
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}



def cart_payment_verify(request):
    user_cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    authority = authority = request.GET['Authority']

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": user_cart.get_total_price(),
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            # return {'status': True, 'RefID': response['RefID']}
            user_cart.is_paid = True
            user_cart.payment_date = timezone.now()
            user_cart.save()
            return HttpResponse('پرداخت موفقیت آمیز بود')
        else:
            # return {'status': False, 'code': str(response['Status'])}
            return HttpResponse('پرداخت با شکست مواجه شد')
        
    return response