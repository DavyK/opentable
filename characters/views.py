from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from characters.models import Character
from characters.forms import CharacterForm
from writeups.models import Writeup, SessionSummary
from django.contrib.auth.decorators import login_required
from opentable.views import get_writeup_archive, get_summary_archive


# Create your views here.
levels = {
     '1': 0,       '2': 2000,     '3': 5000,     '4': 9000,
     '5': 15000,   '6': 23000,    '7': 35000,    '8': 51000,
     '9': 75000,   '10': 105000,  '11': 155000,  '12': 220000,
     '13': 315000, '14': 445000,  '15': 635000,  '16': 890000,
     '17': 1300000,'18': 1800000, '19': 2550000, '20': 3600000}



def list_characters(request):

    characters = Character.objects.all()

    data = {'characters': characters}

    return render_to_response('characters/characterIndex.html', data, context_instance=RequestContext(request))


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
    return render_to_response('characters/characterStats.html', data, context_instance=RequestContext(request))

@login_required
def add_character(request, character_id=None):

    # TODO: currently view sets player as current user if current user is not superuser, maybe change form so that field is autofilled and greyed out

    if character_id is not None:
        this_character = Character.objects.get(pk=character_id)

    if request.method == "POST":
        if character_id is not None:
            character_form = CharacterForm(request.POST, request.FILES, instance=this_character)
        else:
            character_form = CharacterForm(request.POST, request.FILES)

        if character_form.is_valid():
            save_it = character_form.save(commit=False)
            if not request.user.is_superuser:
                save_it.player = request.user
            save_it.save()

            this_character = Character.objects.order_by('-character_updated')[0]
            redirect_to_url = '/showCharacter/{0}/'.format(this_character.id)

            return HttpResponseRedirect(redirect_to_url)


    else:
        if character_id is not None:
            character_form = CharacterForm(instance=this_character)
        else:
            character_form = CharacterForm(None)

    if character_id is not None:
        character_form.helper.form_action = '/editCharacter/' + character_id + '/'

    characters = Character.objects.all()
    data = {'character_form': character_form, 'characters': characters,
            'writeup_archive': get_writeup_archive(), 'summary_archive': get_summary_archive()}

    return render_to_response('characters/addCharacter.html', data, context_instance=RequestContext(request))


def delete_character(request, character_id):

    this_character = Character.objects.get(pk=character_id)
    this_character.delete()

    return HttpResponseRedirect('/')

@login_required
def add_xp(request, character_id):

    #update model with new XP value
    this_character = Character.objects.get(pk=character_id)

    this_character.current_xp += int(request.POST['xp_to_add'])

    if this_character.current_xp >= levels[str(int(this_character.level)+1)]:
        this_character.level += 1

    this_character.save()

    redirect_url = '/showCharacter/'+character_id+'/'
    return HttpResponseRedirect(redirect_url)
