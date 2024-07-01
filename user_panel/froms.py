from django import forms

class ChangeUserInfo(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    meli_code = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    profile_picture = forms.ImageField()
    card_number = forms.CharField()
    forigner = forms.CharField(widget=forms.CheckboxInput())

