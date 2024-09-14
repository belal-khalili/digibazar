from django.urls import path
from . import views 

app_name = 'cart'


urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('increase_cartitem_amount/<int:cartitem_id>',views.plus_cart_item,),
    path('cart_payment',views.cart_payment,name='cart_payment'),
    path('cart_payment_verify/',views.cart_payment_verify,name='cart_payment_verify')
]
