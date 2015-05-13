from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.models import User
from opentable.forms import ChangePasswordForm
# Create your views here.


def list_players(request):

    users = User.objects.all()
    data = {'users': users}
    return render_to_response('players/list_players.html', data, context_instance=RequestContext(request))


def show_player(request, user_id):

    this_user = User.objects.get(pk=user_id)

    data = {'this_user': this_user}
    return render_to_response('players/show_player.html', data, context_instance=RequestContext(request))

