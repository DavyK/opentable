from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from characters.models import Character
from characters.forms import CharacterForm
from writeups.models import Writeup
from django.contrib.auth.decorators import login_required
from opentable.views import get_writeup_archive

# Create your views here.


def home(request):
    characters = Character.objects.all()
    writeups = Writeup.objects.all()
    data = {'characters': characters, 'archive': get_writeup_archive()}
    return render_to_response('characters/characterIndex.html', data, context_instance=RequestContext(request))


def showCharacter(request, character_id):
    thisCharacter = Character.objects.get(pk=character_id)
    characters = Character.objects.all()
    data = {'thisCharacter': thisCharacter, 'characters':characters, 'archive': get_writeup_archive()}
    return render_to_response('characters/characterStats.html', data, context_instance=RequestContext(request))

@login_required
def add_character(request, character_id=None):

    # TODO: currently view sets player as current user if current user is not superuser, maybe change form so that field is autofilled and greyed out

    if character_id is not None:
        thisCharacter = Character.objects.get(pk=character_id)

    if request.method == "POST":
        if character_id is not None:
            character_form = CharacterForm(request.POST, request.FILES, instance=thisCharacter)
        else:
            character_form = CharacterForm(request.POST, request.FILES)

        if character_form.is_valid():
            save_it = character_form.save(commit=False)
            if not request.user.is_superuser:
                save_it.player = request.user
            save_it.save()

            return HttpResponseRedirect('/')


    else:
        if character_id is not None:
            character_form = CharacterForm(instance=thisCharacter)
        else:
            character_form = CharacterForm(None)

    if character_id is not None:
        character_form.helper.form_action = '/editCharacter/' + character_id + '/'

    characters = Character.objects.all()
    data = {'character_form': character_form, 'characters': characters, 'archive': get_writeup_archive()}

    return render_to_response('characters/addCharacter.html', data, context_instance=RequestContext(request))


def delete_character(request, character_id):

    thisCharacter = Character.objects.get(pk=character_id)
    thisCharacter.delete()

    return HttpResponseRedirect('/')
