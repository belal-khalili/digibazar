from django.urls import path
from . import views 

app_name = 'product'


urlpatterns = [
    path('',views.products,name='products_page'),
    path('<slug:slug>/',views.single_product,name='single_product_page'),
]