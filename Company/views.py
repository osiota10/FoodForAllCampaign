from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from foodforallcampaign import settings
from .forms import CreateAccountForm
from Dashboard.models import Profile
from django.contrib.auth.models import User
from .models import *
from . forms import ContactForm, EmailSubscriptionForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template import Context

# Create your views here.


def index(request):
    photo_gallery = PhotoGallery.objects.all()
    testimonials = AllTestimonial.objects.all()

    context = {'photo_gallery': photo_gallery, 'testimonials': testimonials}
    return render(request, 'Company/index.html', context)


def about_us(request):
    context = {}
    return render(request, 'Company/about-us.html', context)


def company_info(request):
    info = CompanyInformation.objects.all()
    core_value = CoreValue.objects.all()
    net_mkt = NetworkMarketing.objects.all().first()
    privacy = PrivacyPolicy.objects.all().first()
    terms_conditions = TermsAndConditions.objects.all().first()
    why_choose_us = WhyChooseUs.objects.all().first()
    services = HowWeWork.objects.all()
    service_list = services
    stat = Stat.objects.all()
    socials = SocialMediaHandle.objects.all()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'ContactForm':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "FFACNG - Quick Contact"
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                with open(settings.BASE_DIR / "templates/ContactForm/ContactFormEmailMsg.txt") as msg:
                    contact_msg = msg.read()
                try:
                    message = EmailMultiAlternatives(subject=subject, body=contact_msg, from_email=settings.EMAIL_HOST_USER, to=[email], headers={'name': name})
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                form.save()
                html_template = get_template("ContactForm/ContactFormEmailMsg.html").render({'name': name})
                message.attach_alternative(html_template, "text/html")
                message.send()

                messages.success(request, 'Contact Details Captured')
        elif request.POST.get("form_type") == 'SubscriptionForm':
            form = EmailSubscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Email Details Captured')
    storage = messages.get_messages(request)
    context = {'info': info, 'core_value': core_value, 'storage': storage,
               'net_mkt': net_mkt, 'services': services, 'privacy': privacy,
               'terms_conditions': terms_conditions, 'why_choose_us': why_choose_us, 'service_list': service_list, 'stat': stat, 'socials': socials}
    return context


class ServicesListView(generic.ListView):
    model = HowWeWork
    context_object_name = 'services'
    template_name = 'Company/services.html'


class ServicesDetailView(generic.DetailView):
    model = HowWeWork
    context_object_name = 'services'
    template_name = 'Company/services-detail.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


def contact(request):
    address_list = BranchAddress.objects.all()
    context = {'address_list': address_list}
    return render(request, 'Company/contact-test.html', context)


def network_marketing(request):
    return render(request, 'Company/network-marketing.html')


def terms_and_conditions(request):
    return render(request, 'Company/terms-and-conditions.html')


def privacy_policy(request):
    return render(request, 'Company/privacy-policy.html')


class PhotoListView(generic.ListView):
    model = PhotoGallery
    context_object_name = 'photos'
    template_name = 'Company/photo-gallery.html'
    paginate_by = 2


def page_not_found_view(request, exception):
    return render(request, 'Company/page-not-found.html', status=404)


class CreateAccountView(generic.CreateView):
    form_class = CreateAccountForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    pk_url_kwarg = 'ref_code'
    # query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        code = str(self.kwargs.get('ref_code'))
        context = super(CreateAccountView, self).get_context_data(**kwargs)
        try:
            pro = Profile.objects.get(code=code)
            self.request.session['ref_profile'] = pro.id
            context['ref_code'] = pro
        except ObjectDoesNotExist:
            context['ref_code'] = "No or Invalid referral Link. Contact Admin"
        return context

    def form_valid(self, form):
        response = super(CreateAccountView, self).form_valid(form)
        profile_id = self.request.session.get('ref_profile')
        if profile_id is not None:
            recommended_by_profile = Profile.objects.get(id=profile_id)

            instance = form.save()
            registered_user = User.objects.get(id=instance.id)
            registered_profile = Profile.objects.get(user=registered_user)
            registered_profile.recommended_by = recommended_by_profile.user
            registered_profile.save()
            return redirect(self.success_url)
        else:
            return response
