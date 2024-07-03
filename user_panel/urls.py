from django.urls import path
from . import views



urlpatterns = [
    path('',views.user_panel,name='profle_page')
]