__author__ = 'davidkavanagh'

from django.conf.urls import patterns, url
from characters import views

urlpatterns = patterns('',
    # Examples:
    url(r'^listCharacters/$', views.list_characters, name='list_characters'),
    url(r'^showCharacter/(?P<character_id>\d+)/$', views.show_character, name='show_character'),
    url(r'^addCharacter/$', views.add_character, name='add_character'),
    url(r'^editCharacter/(?P<character_id>\d+)/$', views.add_character, name='edit_character'),
    url(r'^deleteCharacter/(?P<character_id>\d+)/$', views.delete_character, name='delete_character'),
    url(r'^addXP/(?P<character_id>\d+)/$', views.add_xp, name='add_xp'),
)

