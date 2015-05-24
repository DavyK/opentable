__author__ = 'David Kavanagh'

from .models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field
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

        row1 = Div(
                Div(Field('player'), css_class='col-md-3',),
                Div(Field('character_type'), css_class='col-md-3',),
                Div('name', css_class='col-md-3',),
                Div('race', css_class='col-md-3',),
                css_class='row',
            )

        row2 = Div(
                Div('character_class', css_class='col-md-4',),
                Div('level', css_class='col-md-4',),
                Div('current_xp', css_class='col-md-4'),
                css_class='row',
            )

        row3 = Div(Div('biography', css_class='col-md-12'),css_class='row')

        row4 = Div(
                Div('character_token', css_class='col-md-4'),
                Div('num_deaths', css_class='col-md-4',),
                Div('deceased', css_class='col-md-2',),
                Div('hidden', css_class='col-md-2'),
                css_class='row',
            )

        self.helper.layout = Layout(
            row1,
            row2,
            row3,
            row4
        )

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Character
        fields = ['player', 'character_type', 'name', 'race', 'character_class',
                  'level', 'biography', 'current_xp', 'deceased',
                  'num_deaths', 'character_token', 'hidden']


class CharacterSearchForm(forms.Form):

    PC = ('PC', 'PC')
    NPC = ('NP', 'NPC')
    ORG = ('OR', 'Organisation')
    ALL = ('AL', 'All')

    type_choices = [
        PC,
        NPC,
        ORG,
        ALL
    ]

    type_choices = type_choices

    type = forms.ChoiceField(required=False,
                             choices=type_choices)

    search = forms.CharField()
    deceased_choices = [
        ('a', 'All'),
        ('d', 'Dead'),
        ('n', 'Not Dead')
    ]
    deceased = forms.ChoiceField(required=False,
                                 choices=deceased_choices)

    def __init__(self, *args, **kwargs):
        super(CharacterSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_method = 'Post'
        self.helper.form_action = "/listCharacters/"
        self.helper.layout = Layout(
            InlineField('type'),
            InlineField('deceased'),
            InlineField('search'),
            Submit('Submit', 'Search'),
        )

    class Meta:
        fields = ['type', 'deceased', 'search']