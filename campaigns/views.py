from django.http import request
from django.shortcuts import HttpResponseRedirect, RequestContext, render_to_response
from campaigns.models import Campaign
from campaigns.forms import CampaignForm

# Create your views here.


def list_campaigns(request):

    campaigns = Campaign.objects.all()

    data = {'campaigns': campaigns}

    return render_to_response('campaigns/campaignIndex.html', data, context_instance=RequestContext(request))


def show_campaign(request,campaign_id):

    this_campaign = Campaign.objects.get(pk=campaign_id)

    data = {'this_campaign': this_campaign}

    return render_to_response('campaigns/campaignStats.html', data, context_instance=RequestContext(request))


def add_campaign(request, campaign_id=None):

    if campaign_id is not None:
        this_campaign = Campaign.objects.get(pk=campaign_id)
    else:
        this_campaign = None

    if request.method == "POST":

        campaign_form = CampaignForm(request.POST, instance=this_campaign)

        if campaign_form.is_valid():
            save_it = campaign_form.save(commit=False)
            save_it.save()

            this_campaign = Campaign.objects.order_by('-submission_date')[0]
            redirect_to_url = '/campaigns/showCampaign/{0}/'.format(this_campaign.id)

            return HttpResponseRedirect(redirect_to_url)

    else:
        campaign_form = CampaignForm(instance=this_campaign)

    if campaign_id is not None:
        campaign_form.helper.form_action = '/campaigns/editCampaign/' + campaign_id + '/'

    campaign_form = CampaignForm()
    data = {'campaign_form': campaign_form}
    return render_to_response('campaigns/addCampaign.html', data, context_instance=RequestContext(request))


def delete_campaign(request):

    return HttpResponseRedirect('/listCampaigns/')
