__author__ = 'davidkavanagh'
from django.http import request
from characters.models import Character
from writeups.models import Writeup, SessionSummary, Comment
from django.db.models import Count, Sum, Avg
from collections import Counter
from opentable.views import get_summary_archive, get_writeup_archive

def add_sidebar_data(request):

    data = {}

    data['recently_added_characters'] = Character.objects.order_by('-character_updated')[:5]

    data['writeup_archive'] = get_writeup_archive()

    data['summary_archive'] = get_summary_archive()

    data['character_count'] = Character.objects.all().count()

    data['writeup_count'] = Writeup.objects.all().count()

    data['comment_count'] = Comment.objects.all().count()

    data['summary_count'] = SessionSummary.objects.all().count()

    data['character_deaths'] = Character.objects.aggregate(Sum('num_deaths'))

    data['deceased_characters'] = Character.objects.filter(deceased=True).count()

    data['races'] = Character.objects.values('race').annotate(the_count=Count('race'))

    data['classes'] = Character.objects.values('character_class').annotate(the_count=Count('character_class'))

    data['party_level'] = Character.objects.values('level').aggregate(Sum('level'), Avg('level'))

    return data