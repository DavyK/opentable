__author__ = 'davidkavanagh'

from writeups.models import Writeup, Comment, SessionSummary
from characters.models import Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import InlineCheckboxes
from django import forms


class WriteupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        current_user = kwargs.pop('current_user', None)
        super(WriteupForm, self).__init__(*args, **kwargs)

        if current_user is not None:
            if not current_user.is_superuser:
                current_users = [current_user]
                self.fields['author'].choices = [(u.id, str(u)) for u in current_users]
                author_characters = [(c.id, str(c)) for c in Character.objects.filter(player__pk=current_user.id)]
                self.fields['author_character'].choices = author_characters

            self.initial['author'] = current_user





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
        fields = ['gm', 'number', 'location', 'session_characters',
                  'xp_awarded', 'summary_content', 'important_npcs',
                  'date_added'
                  ]

        widgets = {
            'session_characters': forms.CheckboxSelectMultiple
        }


