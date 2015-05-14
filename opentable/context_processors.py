__author__ = 'davidkavanagh'

from django.http import request
from campaigns.models import Campaign
from characters.models import Character
from writeups.models import Writeup, SessionSummary, Comment
from django.db.models import Count, Sum, Avg
from opentable.views import get_summary_archive, get_writeup_archive
from opentable.forms import LoginForm


def add_sidebar_data(request):

    data = {
        'recently_added_characters': Character.objects.order_by('-character_updated')[:5],
        'recently_added_campaigns' : Campaign.objects.order_by('-submission_date')[:5],
        'writeup_archive': get_writeup_archive(),
        'summary_archive': get_summary_archive(),
        'navbar_login_form': LoginForm()
    }

    return data