from django.shortcuts import render
from account.models import user
from digibazar.profile_photo import settings
from .models import user_profile
# Create your views here
def profiles(request):
    if request.user.profile.picture:
        profile_picture=request.user.profile.url
    else:
        profile_picture=settings.DEFULT_PROFILE
    return render(request,'profile.html',{'profile_picture':profile_picture})
