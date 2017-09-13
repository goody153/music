from django.conf.urls import url

from playlist import views

urlpatterns = [
url(r'^$', views.PlaylistsView.as_view(), name='playlists'),
url(r'^(?P<playlist_id>\d+)/delete/$',views.PlaylistDelete.as_view(),name='delete_playlist'),
]
