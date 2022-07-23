from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='home'),
    path('about', about_us, name='about'),
    path('works', ServicesListView.as_view(), name='services'),
    path('works/<slug:slug>', ServicesDetailView.as_view(), name='services-detail'),
    path('network-marketing', network_marketing, name='network-marketing'),
    path('terms-and-conditions', terms_and_conditions, name='terms-and-conditions'),
    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('photo-gallery', PhotoListView.as_view(), name='photo-gallery'),
    path('contact', contact, name='contact'),
    path('Create-account', CreateAccountView.as_view(), name='register'),
    path('Create-account/<str:ref_code>', CreateAccountView.as_view(), name='register'),
    # path('Create-account/<str:ref_code>', main_view),
    path('reset_password',
         auth_views.PasswordResetView.as_view(template_name='registration/password-reset.html'),
         name='password_reset'),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_sent.html'),
         name='password_reset_done'),
    path('reset/<uid64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset-form.html'),
         name=' password_reset_confirm'),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset-finish.html'),
         name='password_reset_complete'),
]