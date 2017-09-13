from django.conf.urls import url

from playlist import views

urlpatterns = [
url(r'^$', views.PlaylistsView.as_view(), name='playlists'),
]
