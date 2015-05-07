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
        'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive(),
        'character_count': Character.objects.all().count(), 'writeup_count': Writeup.objects.all().count(),
        'comment_count': Comment.objects.all().count(), 'summary_count': SessionSummary.objects.all().count(),
        'character_deaths': Character.objects.aggregate(Sum('num_deaths')),
        'deceased_characters': Character.objects.filter(deceased=True).count(),
        'races': Character.objects.values('race').annotate(the_count=Count('race')),
        'classes': Character.objects.values('character_class').annotate(the_count=Count('character_class')),
        'party_level': Character.objects.values('level').aggregate(Sum('level'), Avg('level')),
        'navbar_login_form': LoginForm()
    }

    return data