__author__ = 'davidkavanagh'

__author__ = 'David Kavanagh'

from writeups.models import Writeup, Comment, SessionSummary
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

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
        fields = ['author', 'author_character', 'title', 'post_content']


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
        self.helper.form_method = 'POST'
        self.helper.form_action = '/writeups/addSummary/'

        self.helper.add_input(Submit('submit', 'Submit'))

        # TODO: Make the character select box in the form show the pictures instead of a list. Use checkboxes instead.

    class Meta:
        model = SessionSummary