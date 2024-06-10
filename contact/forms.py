from django import forms
from .models import Contact

class ContactForm(forms.Form):
    subject = forms.CharField(label="موضوع پیام",
                                max_length=150,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control col-md-12'
                                }))
    full_name = forms.CharField(label="نام و نام خانوادگی",
                                max_length=100,
                                min_length=5,
                                error_messages={'min_length':'حداقل نیاز به ۵ کاراکتر دارید'},
                                widget=forms.TextInput(attrs={
                                    'class':'form-control col-md-12'
                                }))
    email = forms.EmailField(label='ایمیل',
                            max_length=150,
                            error_messages={'invalid':'ایمیل معتبر نمیباشد','required':'ایمیل اجباری میباشد'},
                            widget=forms.EmailInput(attrs={
                                    'class':'form-control col-md-12'
                                }))
    phone_number = forms.CharField(label='شماره تماس',
                                    max_length=13,
                                    widget=forms.TextInput(attrs={
                                        'class':'form-control col-md-12'
                                }))
    text = forms.CharField(label='متن پیام',
                                    widget=forms.Textarea(attrs={
                                    'class':'form-control col-md-12',
                                    'rows':'5',
                                }))
    
class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject','full_name','email','phone_number','text']
        
