from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(label='پسورد')
    confirm_password = forms.CharField(label='تکرار پسورد')
    

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('پسورد شما و تکرار آن با هم مطابق نیستند')
        else:
            return password
        

class LoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(label='پسورد')
