from django.urls import path
from . import views 

app_name = 'category'


urlpatterns = [
    path('<str:catName>/',views.category_view,name='category_page'),
]