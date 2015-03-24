__author__ = 'davidkavanagh'

from django.conf.urls import patterns, include, url
from writeups import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^listWriteups/$', views.list_writeups, name='list_writeups'),
    url(r'^archiveWriteupList/(?P<w_month>\w+)/(?P<w_year>\d+)/$', views.archive_list_writeups, name='archive_list_writeups'),
    url(r'^characterWriteupList/(?P<character_id>\d+)/$', views.character_list_writeups, name='character_list_writeups'),
    url(r'^showWriteup/(?P<writeup_id>\d+)/$', views.show_writeup, name='show_writeup'),
    url(r'^addWriteup/$', views.add_writeup, name='add_writeup'),
    url(r'^editWriteup/(?P<writeup_id>\d+)/$', views.add_writeup, name='edit_writeup'),
    url(r'^deleteWriteup/(?P<writeup_id>\d+)/$', views.delete_writeup, name='delete_writeup'),
    url(r'^addComment/(?P<writeup_id>\d+)/$', views.show_writeup, name='add_comment'),
    url(r'^editComment/(?P<writeup_id>\d+)/(?P<comment_id>\d+)/$', views.show_writeup, name='edit_comment'),
    url(r'^deleteComment/(?P<writeup_id>\d+)/(?P<comment_id>\d+)/$', views.delete_comment, name='delete_comment'),


)