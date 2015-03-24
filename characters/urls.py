__author__ = 'davidkavanagh'

from django.conf.urls import patterns, include, url
from characters import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),

    url(r'^showCharacter/(?P<character_id>\d+)/$', views.showCharacter, name='showCharacter'),
    url(r'^addCharacter/$', views.add_character, name='addCharacter'),
    url(r'^editCharacter/(?P<character_id>\d+)/$', views.add_character, name='editCharacter'),
    url(r'^deleteCharacter/(?P<character_id>\d+)/$', views.delete_character, name='deleteCharacter'),
)

