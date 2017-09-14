from django.conf.urls import url

from playlist import views

urlpatterns = [
    url(r'^playlist/(?P<playlist_id>\d+)/',views.PlaylistView.as_view(),name ="playlist")
]
