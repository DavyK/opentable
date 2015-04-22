__author__ = 'David Kavanagh'

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import RequestContext, render_to_response
from django.core.mail import mail_admins

from writeups.models import Writeup, SessionSummary
from opentable.forms import LoginForm, CustomUserCreationForm


def home(request):

    return render_to_response('opentable/home.html', {}, context_instance=RequestContext(request))


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


def get_writeup_archive():
    archive_dates = Writeup.objects.datetimes('submission_date', 'month', order='DESC')
    return archive_dates


def get_summary_archive():
    archive_dates = SessionSummary.objects.datetimes('session_date', 'month', order='DESC')
    return archive_dates