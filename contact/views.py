from django.shortcuts import render
from .forms import ContactForm,ContactForm2
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact(
                subject=request.POST['subject'],
                full_name=request.POST['full_name'],
                email=request.POST['email'],
                phone_number=request.POST['phone_number'],
                text=request.POST['text'],
            )
            new_contact.save()
        else:
            return render(request,'contact/contact.html',{'form':form})

    return render(request,'contact/contact.html',{'form':ContactForm})