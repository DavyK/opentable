__author__ = 'davidkavanagh'

__author__ = 'David Kavanagh'

from writeups.models import Writeup, Comment
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


