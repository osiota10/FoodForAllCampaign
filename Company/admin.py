from django.contrib import admin
from .models import *

# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "email", "location", "phone_number", "message")
    list_filter = ('date',)


class EmailSubAdmin(admin.ModelAdmin):
    list_display = ("date", "email")
    list_filter = ('date',)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "testimony")
    list_filter = ('location',)


class BranchAddressAdmin(admin.ModelAdmin):
    list_display = ("branch_name", "address", "contact_one")


admin.site.register(AllTestimonial, TestimonialAdmin)
admin.site.register(PhotoGallery)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(CompanyInformation)
admin.site.register(CoreValue)
admin.site.register(HeroMenu)
admin.site.register(HowWeWork)
admin.site.register(EmailSubscription, EmailSubAdmin)
admin.site.register(BranchAddress, BranchAddressAdmin)
admin.site.register(NetworkMarketing)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsAndConditions)
admin.site.register(WhyChooseUs)
admin.site.register(Stat)
admin.site.register(SocialMediaHandle)
