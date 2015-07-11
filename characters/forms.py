__author__ = 'David Kavanagh'

from .models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field
from crispy_forms.bootstrap import InlineField
from django import forms
from django.contrib.auth.models import User

from campaigns.models import Campaign


class CharacterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(CharacterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/addCharacter/"
        self.helper.form_enctype = "multipart/form-data"

        row1 = Div(
            Div('player', css_class='col-md-3',),
            Div('campaign', css_class='col-md-3'),
            Div('character_type', css_class='col-md-3',),
            Div('name', css_class='col-md-3',),
            css_class='row',
        )

        row2 = Div(
            Div('race', css_class='col-md-3',),
            Div('character_class', css_class='col-md-3',),
            Div('level', css_class='col-md-3',),
            Div('current_xp', css_class='col-md-3'),
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
        fields = [
            'player', 'campaign', 'character_type', 'name', 'race', 'character_class',
            'level', 'biography', 'current_xp', 'deceased',
            'num_deaths', 'character_token', 'hidden'
        ]


class CharacterSearchForm(forms.Form):

    player = forms.ModelChoiceField(required=False, queryset=User.objects.all())

    campaigns = Campaign.objects.all()
    campaign = forms.ModelChoiceField(required=False, queryset=campaigns, initial=campaigns[0])

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

    search = forms.CharField(required=False)
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
        self.helper.form_class = 'form'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_method = 'Get'
        self.helper.form_action = "/listCharacters/"
        self.helper.layout = Layout(
            Div(
                Div('campaign', css_class="col-md-6",),
                Div('player', css_class="col-md-6",)
            ),
            Div(
                Div('type', css_class="col-md-6",),
                Div('deceased', css_class="col-md-6",),
            ),
            Div('search', css_class="col-md-12",),
            Submit('Submit', 'Search'),
        )

    class Meta:
        fields = ['campaign', 'player', 'type', 'deceased', 'search']