from django.contrib import admin
from .models import Profile, Withdrawals, Payment, Level, CurrentLevel

# Register your models here.

admin.site.register(Profile)
admin.site.register(Withdrawals)
admin.site.register(Payment)
admin.site.register(Level)
admin.site.register(CurrentLevel)


