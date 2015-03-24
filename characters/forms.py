__author__ = 'David Kavanagh'

from .models import Character
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class CharacterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/addCharacter/"
        self.helper.form_enctype = "multipart/form-data"


        #TODO: Figure out how to get some fields not as wide and inline.

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Character
        fields = ['player', 'name', 'race', 'character_class',
                  'level', 'biography', 'current_xp', 'deceased',
                  'num_deaths', 'character_token']
        '''
        widgets = {
            'player': forms.HiddenInput(),
        }

            'race': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Character Race'}),
            'character_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Character Class'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Backstory'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Comma separated list of tags'}),
        '''
