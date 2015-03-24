__author__ = 'David Kavanagh'

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from writeups.models import Writeup

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

    redirectPath = request.GET['next']
    if redirectPath == '/logout/' or redirectPath is None:
        redirectPath = '/'

    return HttpResponseRedirect(redirectPath)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def get_writeup_archive():
    archive_dates = Writeup.objects.datetimes('submission_date','month', order='DESC')
    return archive_dates