from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from opentable.views import is_gm
from characters.models import Character
from characters.forms import CharacterForm, CharacterSearchForm
from writeups.models import Writeup, SessionSummary

# Create your views here.


#dictionary to hold leveling up XP costs
levels = {
         '1': 0,        '2': 2000,     '3': 5000,     '4': 9000,
         '5': 15000,    '6': 23000,    '7': 35000,    '8': 51000,
         '9': 75000,    '10': 105000,  '11': 155000,  '12': 220000,
         '13': 315000,  '14': 445000,  '15': 635000,  '16': 890000,
         '17': 1300000, '18': 1800000, '19': 2550000, '20': 3600000
}

def list_characters(request, queryset=None):

    if request.method == 'POST':

        characters = Character.objects.all()

        search_text = request.POST['search']
        search_type = request.POST['type']
        search_deceased = request.POST['deceased']

        if search_text:
            characters = characters.filter(Q(name__icontains=search_text) |
                                           Q(character_class__icontains=search_text) |
                                           Q(race__icontains=search_text))

        if search_type !='AL':
            characters = characters.filter(character_type=search_type)


        if search_deceased == 'a':
            pass
        elif search_deceased == 'd':
            characters = characters.filter(deceased=True)
        else:
            characters = characters.filter(deceased=False)

        search_form = CharacterSearchForm(request.POST)

    else:
        if queryset is not None:
            characters = queryset
        else:

            characters = Character.objects.filter(character_type='PC')

        search_form = CharacterSearchForm(None)

    if not is_gm(request.user):
        characters = characters.filter(hidden=False)


    data = {'characters': characters, 'search_form': search_form}
    return render_to_response('characters/list_character.html', data, context_instance=RequestContext(request))


def show_character(request, character_id):

    this_character = Character.objects.get(pk=character_id)

    sessions_in = SessionSummary.objects.filter(session_characters__pk=character_id).count()
    sessions_all = SessionSummary.objects.all().count()

    character_writeups = Writeup.objects.filter(author_character__pk=character_id).count()

    if this_character.level < 20:
        xp_to_next_level = levels[str(this_character.level+1)] - this_character.current_xp
    else:
        xp_to_next_level = '+++'

    characters = Character.objects.all()
    data = {'this_character': this_character, 'characters': characters,
            'sessions_in': sessions_in, 'sessions_all': sessions_all,
            'xp_to_next_level': xp_to_next_level,
            'character_writeups': character_writeups}

    return render_to_response('characters/show_character.html', data, context_instance=RequestContext(request))


@login_required
def add_character(request, character_id=None):

    if character_id is not None:
        this_character = Character.objects.get(pk=character_id)

    if request.method == "POST":
        if character_id is not None:
            character_form = CharacterForm(request.POST, request.FILES, instance=this_character)
            character_form.initial['player'] = this_character.player
        else:
            character_form = CharacterForm(request.POST, request.FILES)

        if character_form.is_valid():
            save_it = character_form.save(commit=False)
            if not request.user.is_superuser:
                save_it.player = request.user
            save_it.save()

            this_character = save_it
            redirect_to_url = '/showCharacter/{0}/'.format(this_character.id)

            return HttpResponseRedirect(redirect_to_url)

    else:
        if character_id is not None:
            character_form = CharacterForm(instance=this_character)
            print this_character.player.id
            character_form.initial['player'] = this_character.player
        else:
            character_form = CharacterForm()

    if character_id is not None:
        character_form.helper.form_action = '/editCharacter/' + character_id + '/'

    if not is_gm(request.user):
        """
        Note that GMs shouldn't be able to make hidden characters or edit the player choice
        """
        character_form.helper.layout[3].pop(3)
        character_form.fields.pop('hidden')
        character_form.fields['player'].choices = [(request.user.id, request.user.username)]


    data = {'character_form': character_form}

    return render_to_response('characters/add_character.html', data, context_instance=RequestContext(request))


def delete_character(request, character_id):

    this_character = Character.objects.get(pk=character_id)
    this_character.delete()

    return HttpResponseRedirect('/')


@login_required
def add_xp(request, character_id):

    # update model with new XP value
    this_character = Character.objects.get(pk=character_id)

    this_character.current_xp += int(request.POST['xp_to_add'])

    # level up
    if this_character.current_xp >= levels[str(int(this_character.level)+1)]:
        this_character.level += 1
        # if got enough XP to level up more than once, reset to XP to XP for next level - 1
        if this_character.current_xp >= levels[str(int(this_character.level)+1)]:
            this_character.current_xp = levels[str(int(this_character.level)+1)] - 1

    this_character.save()

    redirect_url = '/showCharacter/'+character_id+'/'
    return HttpResponseRedirect(redirect_url)


def get_characters_by_player(request, user_id):

    queryset = Character.objects.filter(player__pk=user_id)
    return list_characters(request, queryset)

