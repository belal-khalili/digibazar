from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
       path('', views.blog_page, name='blog_view'),
       path('single-blog/<slug:slug>', views.single_blog, name='single-blog'),
       path('send-blog-comment/',views.send_blog_comment,name='send_blog_comment')
]