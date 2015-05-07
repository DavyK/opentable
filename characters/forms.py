__author__ = 'David Kavanagh'

from .models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field
from crispy_forms.bootstrap import InlineField
from django import forms


class CharacterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        current_user = kwargs.pop('current_user', None)

        super(CharacterForm, self).__init__(*args, **kwargs)

        self.initial['player'] = current_user

        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/addCharacter/"
        self.helper.form_enctype = "multipart/form-data"

        self.helper.layout = Layout(
            Div(
                Div(Field('player'), css_class='col-md-4',),
                Div('name', css_class='col-md-4',),
                Div('race', css_class='col-md-4',),
                css_class='row',
            ),
            Div(
                Div('character_class', css_class='col-md-4',),
                Div('level', css_class='col-md-4',),
                Div('current_xp', css_class='col-md-4'),
                css_class='row',
            ),
            Div(Div('biography', css_class='col-md-12'),css_class='row'),
            Div(
                Div('num_deaths', css_class='col-md-4',),
                Div('deceased', css_class='col-md-4',),
                Div('character_token', css_class='col-md-4'),
                css_class='row',
            ),

        )

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