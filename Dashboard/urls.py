from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('referrals', referral_view, name='referrals'),
    path('withdrawals', withdrawals, name='withdrawals'),
    path('make-payments', payments, name='payments'),
    path('levels', levels, name='levels'),
    path('downlines', downlines, name='downlines'),
    path('edit-profile', EditProfileView.as_view(), name='edit-profile'),
]
