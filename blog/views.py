from django.shortcuts import render
from .models import veblog
from django.core.paginator import Paginator
# Create your views here.

def blog_page(request):
    data = veblog.objects.all()
    paginator = Paginator(data,5)
    page_number = request.GET.get('page')
    this_page = paginator.get_page(page_number)
    recent_blog = veblog.objects.all().order_by('-id')[:3]
    return render(request, 'blog/blog.html', {'blogs':data, 'recent_blog':recent_blog, 'this_page':this_page, 'paginator':paginator})



def single_blog(request,slug):
    data=veblog.objects.get(slug=slug``)
    return render(request,'blog/single-blog.html', {'blog' : data})
