from django.shortcuts import render

# Create your views here.

def user_panel(request):
    return render(request,'user_panel/user_panel.html')
