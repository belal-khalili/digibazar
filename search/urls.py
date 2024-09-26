from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('',views.search_product,name='search'),
    path('live_search/',views.live_search,name='live_search')
]