__author__ = 'davidkavanagh'

from django.conf.urls import patterns, url
from players import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^listPlayers/$', views.list_players, name='list_players'),
                       url(r'^showPlayer/(?P<user_id>\d+)/$', views.show_player, name='show_player'),
                       # url(r'^addplayer/$', views.add_player, name='add_player'),
                       # url(r'^editplayer/(?P<player_id>\d+)/$', views.edit_player, name='edit_player'),
                       # url(r'^deleteplayer/(?P<player_id>\d+)/$', views.delete_player, name='delete_player'),
                       )