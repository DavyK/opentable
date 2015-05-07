from django.http import request
from django.shortcuts import HttpResponseRedirect, RequestContext, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from campaigns.models import Campaign
from campaigns.forms import CampaignForm

# Create your views here.


def list_campaigns(request):

    page = request.GET.get('page')

    campaigns_queryset = Campaign.objects.all()

    paginator = Paginator(campaigns_queryset, 10)

    pages = [i+1 for i in range(paginator.num_pages)]

    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        campaigns = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        campaigns = paginator.page(paginator.num_pages)

    data = {'campaigns': campaigns}

    return render_to_response('campaigns/index_campaign.html', data, context_instance=RequestContext(request))


def show_campaign(request,campaign_id):

    this_campaign = Campaign.objects.get(pk=campaign_id)

    data = {'this_campaign': this_campaign}

    return render_to_response('campaigns/show_campaign.html', data, context_instance=RequestContext(request))


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

    data = {'campaign_form': campaign_form}
    return render_to_response('campaigns/add_campaign.html', data, context_instance=RequestContext(request))


def delete_campaign(request, campaign_id):

    this_campaign = Campaign.objects.get(pk=campaign_id)

    this_campaign.delete()

    return HttpResponseRedirect('/campaigns/listCampaigns/')
