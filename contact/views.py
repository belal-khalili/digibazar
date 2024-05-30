from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
        else:
            return render(request,'contact/contact.html',{'form':form})

    return render(request,'contact/contact.html',{'form':ContactForm})