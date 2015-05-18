__author__ = 'David Kavanagh'
from itertools import chain
from operator import attrgetter

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import RequestContext, render_to_response
from django.core.mail import mail_admins
from django.contrib.auth.decorators import login_required


from campaigns.models import Campaign
from characters.models import Character
from writeups.models import Writeup, SessionSummary, Comment
from django.db.models import Count, Sum, Avg
from writeups.models import Writeup, SessionSummary
from opentable.forms import LoginForm, CustomUserCreationForm, ChangePasswordForm

def home(request):

    return render_to_response('opentable/home.html', {}, context_instance=RequestContext(request))


def numbers(request):

    data = {
        'character_count': Character.objects.all().count(),
        'writeup_count': Writeup.objects.all().count(),
        'comment_count': Comment.objects.all().count(),
        'summary_count': SessionSummary.objects.all().count(),
        'character_deaths': Character.objects.aggregate(Sum('num_deaths')),
        'deceased_characters': Character.objects.filter(deceased=True).count(),
        'races': Character.objects.values('race').annotate(the_count=Count('race')),
        'classes': Character.objects.values('character_class').annotate(the_count=Count('character_class')),
        'party_level': Character.objects.values('level').aggregate(Sum('level'), Avg('level')),
    }

    return render_to_response('opentable/numbers.html', data, context_instance=RequestContext(request))

def about(request):

    return render_to_response('opentable/about.html', {}, context_instance=RequestContext(request))

def user_login(request):

    login_form = LoginForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    redirect_path = request.GET['next']
                    return HttpResponseRedirect(redirect_path)
                else:
                    login_form.add_error(None, "Your account has not yet been activated.")

    if 'next' in request.GET.keys():
        next_page = request.GET['next']
    else:
        next_page = '/'

    return render_to_response('opentable/login.html',
                              {'login_form': login_form, 'next_page': next_page},
                              context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_new_user(request):

    new_user_form = CustomUserCreationForm()

    if request.method == 'POST':
        new_user_form = CustomUserCreationForm(request.POST)

        if new_user_form.is_valid():
            new_user = new_user_form.save(commit=False)
            new_user.is_active = False
            new_user.save()


            email_subject = u'Ptolus Open Table - New User'

            email_msg = u"""
            A new user has registered to the ptolus open table site.
            Please review their details and activate them if approved.
            """

            mail_admins(email_subject, email_msg, fail_silently=False)

            return HttpResponseRedirect('/')

    data = {'new_user_form': new_user_form}

    return render_to_response('opentable/register.html', data, context_instance=RequestContext(request))

@login_required
def change_password(request, user_id):

    this_user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        change_password_form = ChangePasswordForm(request.POST)

        if change_password_form.is_valid(this_user):
            this_user.set_password(change_password_form.cleaned_data['new_password1'])
            this_user.save()
            redirect_url = '/players/showPlayer/{0}/'.format(this_user.id)

            return HttpResponseRedirect(redirect_url)
    else:
        change_password_form = ChangePasswordForm()

    print change_password_form.fields

    data = {'change_password_form': change_password_form}

    return render_to_response('opentable/change_password.html', data, context_instance=RequestContext(request))


def get_writeup_archive():
    archive_dates = Writeup.objects.datetimes('date_added', 'month', order='DESC')
    return archive_dates


def get_summary_archive():
    archive_dates = SessionSummary.objects.datetimes('date_added', 'month', order='DESC')
    return archive_dates
