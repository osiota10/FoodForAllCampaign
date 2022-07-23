from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.


class AllTestimonial(models.Model):
    photo = CloudinaryField('image')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=15)
    testimony = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/Images/default-user.jfif"


class PhotoGallery(models.Model):
    photo = CloudinaryField('image')

    class Meta:
        verbose_name_plural = "Photo Gallery"

    def __str__(self):
        return f"{self.photo}"


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Us"


class EmailSubscription(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.email}"


class CompanyInformation(models.Model):
    logo = CloudinaryField('image')
    page_header_image = CloudinaryField(null=True, blank=True)
    name = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=50)
    email = models.EmailField()
    history = RichTextField(blank=True, null=True)
    history_image = CloudinaryField('image', null=True, blank=True)
    about = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Company Information"

    def __str__(self):
        return f"{self.name}-{self.telephone}"


class BranchAddress(models.Model):
    branch_name = models.CharField(max_length=20)
    address = models.TextField()
    contact_one = models.CharField(max_length=11)
    contact_two = models.CharField(max_length=11, blank=True, null=True)
    contact_three = models.CharField(max_length=11, blank=True, null=True)
    contact_four = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Branch Addresses"

    def __str__(self):
        return f"{self.branch_name}"


class CoreValue(models.Model):
    font_awesome_class = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)
    message = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class HeroMenu(models.Model):
    pic = CloudinaryField('image')
    title = models.CharField(max_length=50)
    snippet = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Hero Menu"


class OtherWebPages(models.Model):
    pic = CloudinaryField('image')
    title = models.CharField(max_length=50)
    snippet = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Other Web Pages"
        # ordering = ['pk']

    def __str__(self):
        return f"{self.title}"


class HowWeWork(models.Model):
    pic = CloudinaryField('image')
    slug = models.SlugField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=50)
    snippet = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "How We Work"

    @property
    def get_photo_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url
        else:
            return "/static/Images/default-user.jfif"

    def __str__(self):
        return f"{self.title}"


class NetworkMarketing(models.Model):
    pic = CloudinaryField('image')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, blank=True, null=True)
    snippet = RichTextField()

    class Meta:
        verbose_name_plural = "Network Marketing"
        # ordering = ['pk']

    def __str__(self):
        return f"{self.title}"


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=50)
    snippet = RichTextField()

    class Meta:
        verbose_name_plural = "Privacy Policy"
        # ordering = ['pk']

    def __str__(self):
        return f"{self.title}"


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=50)
    snippet = RichTextField()

    class Meta:
        verbose_name_plural = "Terms And Conditions"
        # ordering = ['pk']

    def __str__(self):
        return f"{self.title}"


class WhyChooseUs(models.Model):
    pic = CloudinaryField('image', blank=True, null=True)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, blank=True, null=True)
    snippet = RichTextField()

    class Meta:
        verbose_name_plural = "Why Choose Us"
        # ordering = ['pk']

    def __str__(self):
        return f"{self.title}"


class Stat(models.Model):
    font_awesome_class = models.CharField(max_length=30)
    stat_figure = models.IntegerField()
    stat_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.stat_title}-{self.stat_figure}"


class SocialMediaHandle(models.Model):
    font_awesome_class = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.name}"
