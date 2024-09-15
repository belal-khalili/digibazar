from django.shortcuts import render
from .models import Blog,BlogComment
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
# Create your views here.

def blog_page(request):
    data = Blog.objects.all()
    paginator = Paginator(data,5)
    page_number = request.GET.get('page')
    this_page = paginator.get_page(page_number)
    recent_blog = Blog.objects.all().order_by('-id')[:3]
    return render(request, 'blog/blog.html', {'blogs':data, 'recent_blog':recent_blog, 'this_page':this_page, 'paginator':paginator})



def single_blog(request,slug):
    blog=Blog.objects.get(slug=slug)
    blog_comments = BlogComment.objects.filter(blog=blog, admin_verify=True, parent=None).order_by('-date')
    return render(request,'blog/single-blog.html', {'blog' : blog, 'blog_comments':blog_comments})


def send_blog_comment(request):
    data = json.loads(request.body)
    print(request.user)
    # print(x)
    this_blog = Blog.objects.get(id=data.get('blogid'))

    new_comment = BlogComment(
        user=request.user,
        blog=this_blog,
        text= data.get('comment_text')
    )
    new_comment.save()


    return JsonResponse({'status':'ok'})