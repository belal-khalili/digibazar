from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def add_to_cart(request,product_id):
    print('*'*90)
    print(product_id)
    print('*'*90)
    return JsonResponse({'status':'ok', 'message':'soma kheyli khobid'})