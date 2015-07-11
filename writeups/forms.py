__author__ = 'davidkavanagh'

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import Field, InlineCheckboxes
from django import forms
from django.contrib.auth.models import User

from writeups.models import Writeup, Comment, SessionSummary
from characters.models import Character
from campaigns.models import Campaign


class WriteupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(WriteupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/writeups/addWriteup/"

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Writeup
        fields = ['author', 'author_character', 'date_added', 'post_content', ]


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/writeups/addComment/"

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Comment
        fields = ['comment_content']


class SummaryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SummaryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_id = 'summary-add-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '/writeups/addSummary/'

        self.helper.layout = Layout(
            Div(
                Div('gm', css_class='col-md-6',),
                Div('number', css_class='col-md-6',),
                css_class='row',
            ),
            'location',
            InlineCheckboxes('session_characters'),
            'summary_content',
            Div(
                Div('important_npcs', css_class='col-md-4',),
                Div('xp_awarded', css_class='col-md-4',),
                Div('date_added', css_class='col-md-4'),
                css_class='row',
            ),
        )

        self.helper.add_input(Submit('submit', 'Submit'))

        # TODO: Make the character select box in the form show the pictures instead of a list. Use checkboxes instead.

    class Meta:
        model = SessionSummary
        fields = [
            'gm', 'number', 'location', 'session_characters',
            'xp_awarded', 'summary_content', 'important_npcs',
            'date_added'
        ]

        widgets = {
            'session_characters': forms.CheckboxSelectMultiple
        }


class WriteupSearchForm(forms.Form):

    campaigns = Campaign.objects.all()
    campaign = forms.ModelChoiceField(required=False, queryset=campaigns)

    player = forms.ModelChoiceField(required=False, queryset=User.objects.all())

    characters = Character.objects.all()
    character = forms.ModelChoiceField(required=False, queryset=characters)

    date_range_start = forms.DateTimeField(required=False)
    date_range_end = forms.DateTimeField(required=False)


    sort_by = forms.ChoiceField(required=False,
                                choices=([('R', 'Recent'),('O', 'Oldest')]),
                                initial='O',
                                widget=forms.Select())



    search_text = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(WriteupSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'writeup-search-form'
        self.helper.form_class = 'form'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_method = 'Get'
        self.helper.form_action = "/writeups/listWriteups/"
        self.helper.layout = Layout(
            Div(
                Div('player', css_class='col-md-6',),
                Div('character', css_class='col-md-6',)
            ),
            Div(
                Div('date_range_start', css_class='col-md-4',),
                Div('date_range_end', css_class='col-md-4',),
                Div('sort_by', css_class='col-md-4',)
            ),
            Div(
                Div('search_text', css_class='col-md-12',)
            ),
            
            Submit('Submit', 'Search'),
        )

    class Meta:
        fields = ['campaign', 'player', 'character', 'search_text']


