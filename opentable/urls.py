from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from opentable import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'opentable.views.home', name='home'),
    url(r'^', include('characters.urls', namespace='characters')),
    url(r'^writeups/', include('writeups.urls', namespace='writeups')),
    url(r'^campaigns/', include('campaigns.urls', namespace='campaigns')),
    url(r'^players/', include('players.urls', namespace='players')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'opentable.views.user_login', name='login'),
    url(r'^logout/', 'opentable.views.user_logout', name='logout'),
    url(r'^register/', 'opentable.views.register_new_user', name='register_new_user'),
    url(r'^changePassword/(?P<user_id>\d+)/$', 'opentable.views.change_password', name='change_password'),
    url(r'^tinymce/', include('tinymce.urls')),

)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )

