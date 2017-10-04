from django.conf.urls import url

from .views import (
    AllPlaylistView,
    PlaylistView,
    SongDetail,
    SongDelete,
    PlaylistDelete
    )

urlpatterns = [
    url(r'^$', AllPlaylistView.as_view(), name='all_playlist'),
    url(r'^playlist/(?P<playlist_id>\d+)/$', PlaylistView.as_view(), name='playlist'),
    url(r'^playlist/(?P<playlist_id>\d+)/(?P<song_id>\d+)/$', SongDetail.as_view(), name='song_detail'),
    url(r'^playlist/(?P<playlist_id>\d+)/(?P<song_id>\d+)/delete/$', SongDelete.as_view(), name='song_delete'),
    url(r'^playlist/(?P<playlist_id>\d+)/delete/$', PlaylistDelete.as_view(), name='playlist_delete')
]