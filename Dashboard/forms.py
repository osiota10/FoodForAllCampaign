from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from Dashboard.models import Profile, Withdrawals, Payment


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'code', 'recommended_by', 'status']


class WithdrawalForm(ModelForm):
    class Meta:
        model = Withdrawals
        fields = ['amount']


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']
