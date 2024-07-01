from django.urls import path
from . import views
urlpatterns = [
    path('',views.profile_page,name='profile_page'),
    path('info/',views.profile_info,name='profile_info'),
]