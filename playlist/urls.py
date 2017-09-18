from django.conf.urls import url

from playlist import views

urlpatterns = [
    url(r'^$', views.PlaylistsView.as_view(), name ="playlists"),
    url(r'^playlist/(?P<playlist_id>\d+)/$', views.PlaylistView.as_view(), name ="playlist"),
    url(r'^playlist/(?P<playlist_id>\d+)/(?P<song_id>\d+)/$', views.SongDetail.as_view(), name ="song_detail"),
    url(r'^playlist/(?P<playlist_id>\d+)/(?P<song_id>\d+)/delete/$', views.SongDelete.as_view(), name ="song_delete"),
]
