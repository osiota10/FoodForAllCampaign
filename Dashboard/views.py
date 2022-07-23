from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Withdrawals, User, Level, CurrentLevel
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from Company.forms import CreateAccountForm
from .forms import EditProfileForm, WithdrawalForm, PaymentForm
from django.core.paginator import Paginator
from .utils import reverse, get_downlines_slice, get_last_item, Node
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages.views import SuccessMessageMixin
from binarytree import build


def dashboard(request):
    # referral queryset
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profile()[:3]

    # index slice from Utils for lastest downline
    index_slice = get_downlines_slice(username=request.user)[:3]

    # Profile Info Query
    profile = Profile.objects.get(user=request.user)

    # withdrawals history query
    with_history = User.objects.get(username=request.user)
    all_history = with_history.withdrawals_set.all()[:3]

    # downline number and Current Level
    level_info = Level.objects.all()
    downline_slice = get_downlines_slice(username=request.user)
    downline_number = len(downline_slice)
    all_level_downline_list = Level.get_level_downline_list(request.user)
    last_item = get_last_item(downline_number, all_level_downline_list)
    current_level = Level.objects.get(down_lines=last_item)

    context = {'my_recs': my_recs, 'profile': profile, 'all_history': all_history,
               'downline_number': downline_number, 'current_level': current_level, 'index_slice': index_slice}
    return render(request, 'dashboard.html', context)


def referral_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profile()
    # paginator
    paginator = Paginator(my_recs, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    my_recs_count = len(my_recs)
    context = {'page_obj': page_obj, 'my_recs_count': my_recs_count, 'profile': profile}
    return render(request, 'referrals.html', context)


def withdrawals(request):
    # Query for total Referral
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommended_profile()
    my_recs_count = len(my_recs)

    # withdrawals history query
    with_history = User.objects.get(username=request.user)
    all_history = with_history.withdrawals_set.all()
    total_withdrawals = all_history.count()
    approved_withdrawals = all_history.filter(status='Approved').count()

    # paginator
    paginator = Paginator(all_history, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # Form
    form_class = WithdrawalForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form = form.save()
            return redirect('withdrawals')
        else:
            form = WithdrawalForm()
    print(form)
    context = {'my_recs_count': my_recs_count, 'profile': profile, 'page_obj': page_obj,
               'total_withdrawals': total_withdrawals, 'approved_withdrawals': approved_withdrawals, 'form': form}

    return render(request, 'withdrawals.html', context)


def payments(request):
    # Query for Payments History
    payment_history = User.objects.get(username=request.user)
    all_payment_history = payment_history.payment_set.all()
    all_payment_count = all_payment_history.count()

    # paginator
    paginator = Paginator(all_payment_history, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # Form
    form_class = PaymentForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form = form.save()
            return redirect('payments')
        else:
            form = PaymentForm()

    pending_payments = all_payment_history.filter(status='Pending').count()
    approved_payments = all_payment_history.filter(status='Approved').count()
    rejected_payments = all_payment_history.filter(status='Rejected').count()
    context = {'page_obj': page_obj, 'all_payment_count': all_payment_count,
               'pending_payments': pending_payments, 'approved_payments': approved_payments,
               'rejected_payments': rejected_payments}
    return render(request, 'payments.html', context)


def levels(request):
    level_info = Level.objects.all()
    downline_slice = get_downlines_slice(username=request.user)
    downline_number = len(downline_slice)
    all_level_downline_list = Level.get_level_downline_list(request.user)
    last_item = get_last_item(downline_number, all_level_downline_list)
    current_level = Level.objects.get(down_lines=last_item)

    context = {'level_info': level_info, 'current_level': current_level, 'downline_number': downline_number}
    return render(request, 'levels.html', context)


def downlines(request):
    # index slice from Utils
    index_slice = get_downlines_slice(username=request.user)

    # testing from binary tree module
    all_users = User.objects.all()
    all_userss = User.objects.get(username=request.user)
    recommended_by = all_userss.profile.recommended_by
    print(recommended_by)
    all_profile = Profile.objects.all()

    all_users = User.objects.all()
    first_user = all_users.first()

    qs = []
    for users in all_users:
        qs.append(users.username)

    root = Node(first_user)

    for items in qs:
        root.insert(items)
    # print(qs)
    root.print_tree()

    # paginator
    paginator = Paginator(index_slice, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    # downlines Stat
    current_downlines = len(index_slice)
    total_downlines = 256
    remaining_downlines = total_downlines - current_downlines
    context = {'index_slice': index_slice, 'current_downlines': current_downlines,
               'total_downlines': total_downlines, 'remaining_downlines': remaining_downlines, 'page_obj': page_obj}
    return render(request, 'downlines.html', context)


class EditProfileView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'update-profile.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Profile successfully Updated"

    def get_object(self, queryset=None):
        current_user = Profile.objects.get(user=self.request.user)
        return current_user
