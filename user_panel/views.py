from django.shortcuts import render
from .froms import ChangeUserInfo
from django.forms.models import model_to_dict
from account.models import User


# Create your views here.
def profile_page(request):
    return render(request,'user_panel/user_panel.html')




def profile_info(request):
    print(request.user.id)
    myuser = User.objects.get(id=request.user.id)
    form = ChangeUserInfo(initial=model_to_dict(myuser))
    print(request.POST)
    return render(request,'user_panel/profile_info.html',{'form':form})

