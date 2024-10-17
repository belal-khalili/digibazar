from django.shortcuts import render
from product.models import Product
from django.http import JsonResponse
from django.core.serializers import serialize
import json

# Create your views here.
def search_product(request):
    if request.method == 'POST':
        search_result = Product.objects.filter(title__icontains=request.POST.get('search_keyword'))
        return render(request,'shared/base.html',{'result':search_result})
    else:
        return render(request,'shared/base.html')


def live_search(request):
    data = json.loads(request.body)
    if len(data.get('search_keyword')) > 0:
        search_result = Product.objects.filter(title__icontains=data.get('search_keyword'))
        myjson = json.loads(serialize('json',search_result))
        # print(myjson)
        return JsonResponse({'data':myjson})
    

