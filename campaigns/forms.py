__author__ = 'davidkavanagh'

from campaigns.models import Campaign
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import InlineField
from django import forms



class CampaignForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'bootstrap3'
        self.helper.form_method = 'POST'
        self.helper.form_action = "/campaigns/addCampaign/"

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Campaign
        fields = ['name', 'rule_set', 'description']

