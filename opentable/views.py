__author__ = 'David Kavanagh'

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, RequestContext, render_to_response
from django.contrib.auth.forms import UserCreationForm
from characters.models import Character
from writeups.models import Writeup, SessionSummary


def home(request):

    return render_to_response('opentable/home.html', {}, context_instance=RequestContext(request))


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                redirectPath = request.GET['next']
                print redirectPath
                return HttpResponseRedirect(redirectPath)
        else:
            return HttpResponseRedirect('/')

    else:
        next_page = request.GET['next']
        return render_to_response('opentable/login.html', {'next_page': next_page}, context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_new_user(request):

    new_user_form = UserCreationForm()

    if request.method == 'POST':
        new_user_form = UserCreationForm(request.POST)
        print 'test1'
        if new_user_form.is_valid():
            print 'test2'
            print new_user_form.cleaned_data.keys()
            new_user = new_user_form.save(commit=False)

            print new_user.is_active

            new_user.set_password(new_user.password)
            new_user.is_active = False

            print new_user.is_active

            new_user.save()

            return HttpResponseRedirect('/')



    data = {'new_user_form': new_user_form}

    return render_to_response('opentable/register.html', data, context_instance=RequestContext(request))


def get_writeup_archive():
    archive_dates = Writeup.objects.datetimes('submission_date','month', order='DESC')
    return archive_dates

def get_summary_archive():
    archive_dates = SessionSummary.objects.datetimes('session_date', 'month', order='DESC')
    return archive_dates