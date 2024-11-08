from django.urls import path
from . import views 

app_name = 'product'


urlpatterns = [
    path('',views.products,name='products_page'),
    path('filter/',views.product_filter,name='product_filter_page'),
    path('filter_result/',views.filter_result, name='filter_result_page'),
    path('<slug:slug>/',views.single_product,name='single_product_page'),
]