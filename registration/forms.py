from django.forms import ModelForm
from django import forms
from .models import CustomUser
class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'phone_number')
