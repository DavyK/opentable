from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from characters.models import Character


# Create your views here.

@login_required
def list_players(request):
    users = User.objects.all()

    character_counts = User.objects.all().annotate(Count('character'))

    writeup_counts = User.objects.all().annotate(Count('writeup'))

    character2player = {i['name']: i['player__username'] for i in Character.objects.values('name', 'player__username')}
    character_session_counts = Character.objects.all().annotate(Count('sessionsummary'))

    player_session_counts = {}

    for i in character_session_counts:
        username = character2player[i.name]
        player_session_counts.setdefault(username, 0)
        player_session_counts[username] += i.sessionsummary__count

    session_counts = []
    for u in users:
        try:
            count = player_session_counts[u.username]
        except KeyError:
            count = 0
        session_counts.append(count)

    user_data = zip(users, character_counts, writeup_counts, session_counts)
    data = {
        'user_data': user_data,
    }
    return render_to_response('players/list_players.html', data, context_instance=RequestContext(request))


@login_required
def show_player(request, user_id):
    this_user = User.objects.get(pk=user_id)

    data = {'this_user': this_user}
    return render_to_response('players/show_player.html', data, context_instance=RequestContext(request))

