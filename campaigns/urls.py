__author__ = 'davidkavanagh'

from django.conf.urls import patterns, url
from campaigns import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.list_campaigns, name='list_campaigns'),
    url(r'^listCampaigns/$', views.list_campaigns, name='list_campaigns'),
    url(r'^showCampaign/(?P<campaign_id>\d+)/$', views.show_campaign, name='show_campaign'),
    url(r'^addCampaign/$', views.add_campaign, name='add_campaign'),
    url(r'^editCampaign/(?P<campaign_id>\d+)/$', views.add_campaign, name='edit_campaign'),
    url(r'^deleteCampaign/(?P<campaign_id>\d+)/$', views.delete_campaign, name='delete_campaign'),
)