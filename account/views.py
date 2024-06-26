from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from .models import User
from django.contrib.auth import logout,login
from django.urls import reverse
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user_email = request.POST.get('email')
            user_username = request.POST.get('username')
            user_password = request.POST.get('password')
            user_confirm_password = request.POST.get('confirm_password')

            user = User.objects.filter(email__iexact=user_email).first()
            if user == None:
                new_user = User(email=user_email,username =user_username,is_active=False)
                new_user.set_password(user_password)
                new_user.save()
            else:
                form.add_error('email','این ایمیل تکراری میباشد')
                return render(request,'account/register.html',{'form':form})
        else:
            return render(request,'account/register.html',{'form':form})

    return render(request,'account/register.html',{'form':RegisterForm})


def logout_view(request):
    logout(request)
    return redirect(reverse('home:home_page'))

def login_view(request):
    return render(request,'account/login.html',{'form':LoginForm})
