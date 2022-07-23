from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateAccountForm(UserCreationForm):
    # pin = forms.CharField(max_length=10,
    #                       widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'pin'}))
    # your_referral = forms.CharField(max_length=100,
    #                                 widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'your_referral'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control inputfield', 'id': 'first_name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control inputfield', 'id': 'last_name'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control inputfield', 'id': 'password1'}))
    password2 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control inputfield', 'id': 'password2'}))

    # def __init__(self, *args, **kwargs):
    #     super(CreateAccountForm, self).__init__(*args, **kwargs)
    #     self.fields['your_referral'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control inputfield', 'id': 'username', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control inputfield', 'id': 'inputEmail4'}),
        }


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


class EmailSubscriptionForm(ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email']
