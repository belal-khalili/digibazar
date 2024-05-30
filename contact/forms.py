from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="نام و نام خانوادگی", max_length=100,min_length=5,error_messages={'min_length':'حداقل نیاز به ۵ کاراکتر دارید'})
    email = forms.EmailField(label='ایمیل خود را وارد کنید', max_length=150,error_messages={'invalid':'ایمیل معتبر نمیباشد','required':'ایمیل اجباری میباشد'})
    phone_number = forms.CharField(label='شماره تماس', max_length=13)
    text = forms.CharField(label='متن پیام')
