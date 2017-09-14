from django.conf.urls import url

from playlist import views

urlpatterns = [
    url(r'^playlist/', )
]
from django.conf.urls import url


urlpatterns = [
    url(r'^playlist/(?P<playlist_id>\d+)/$', PlaylistView.as_view(),name = 'playlist'),
]