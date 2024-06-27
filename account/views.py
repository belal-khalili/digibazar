from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from .models import User
from django.contrib.auth import logout,login
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from random import randint

# Create your views here.
def send_verification_email(reciver, v_code):
    subject = 'به سایت دیجی بازار خوش آمدید هوررررررا'
    message = f'کد تایید شما در دیجی بازار {v_code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [reciver]
    send_mail( subject, message, email_from, recipient_list )



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
                verification_code = randint(10000,99999)
                send_verification_email(new_user.email,verification_code)
                new_user.v_code = verification_code
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(email__iexact=request.POST.get('email'))
            passowrd_valid = user.check_password(request.POST.get('password'))
            if passowrd_valid:
                login(request,user)
                return redirect(reverse('home:home_page'))
            else:
                form.add_error('password','پسورد یا ایمیل وارد شده صحیح نمیباشد')
                return render(request,'account/login.html',{'form':form})
            
    return render(request,'account/login.html',{'form':LoginForm})


def activate_account(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        if user.v_code == password:
            user.is_active = True
            user.v_code = None
            user.save()
            return redirect(reverse('account:login_page'))
    return render(request, 'account/activate_account.html')