from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code, generate_payment_pin, get_downlines_slice
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    STATUS = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    other_name = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True, choices=GENDER)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CharField, blank=True, null=True, related_name='ref_by')
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    account_name = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Inactive', null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    local_government = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)


    @property
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/Images/default-user.jfif"

    def __str__(self):
        return f"{self.user.username}-{self.code}"

    def get_recommended_profile(self):
        qs = Profile.objects.all()
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self.user and profile.status == 'Active':
                my_recs.append(profile)
        return my_recs

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)


class Withdrawals(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')
    current_balance = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username}-{self.amount}"


class Payment(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    pin = models.CharField(max_length=5, blank=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

    def __str__(self):
        return f"{self.user.username}-{self.amount}"

    def save(self, *args, **kwargs):
        if self.pin == "":
            pin = generate_payment_pin()
            self.pin = pin
        super().save(*args, **kwargs)


class Level(models.Model):
    LEVELS = [
        ('Level 0', 'Level 0'),
        ('Level 1', 'Level 1'),
        ('Level 2', 'Level 2'),
        ('Level 3', 'Level 3'),
        ('Level 4', 'Level 4'),
        ('Level 5', 'Level 5'),
        ('Level 6', 'Level 6'),
        ('Level 7', 'Level 7'),
        ('Level 8', 'Level 8'),
    ]
    level = models.CharField(max_length=50, choices=LEVELS)
    down_lines = models.IntegerField(blank=True, null=True)
    referral_bonus = models.IntegerField(blank=True, null=True)
    match_bonus = models.IntegerField(blank=True, null=True)
    upgrade_payment = models.IntegerField(blank=True, null=True)
    reward = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.level}"

    def get_level_downline_list(self):
        level_downline = Level.objects.all()
        qs = []
        for downline in level_downline:
            lst = downline.down_lines
            qs.append(lst)
        return qs

    def get_referral_bonus(self):
        pass

    def get_match_bonus(self):
        pass

    def get_upgrade_payment(self):
        pass


class CurrentLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user}-{self.level}"
