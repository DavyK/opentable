__author__ = 'David Kavanagh'

from .models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import InlineField
from django import forms


class CharacterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/addCharacter/"
        self.helper.form_enctype = "multipart/form-data"

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Character
        fields = ['player', 'name', 'race', 'character_class',
                  'level', 'biography', 'current_xp', 'deceased',
                  'num_deaths', 'character_token']


class CharacterSearchForm(forms.Form):

    search = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(CharacterSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_method = 'Post'
        self.helper.form_action = "/listCharacters/"
        self.helper.layout = Layout(
            InlineField('search'),
            Submit('Submit', 'Search'),
        )

    class Meta:
        fields = ['search']