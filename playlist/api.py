from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class PlaylistViewSet(viewsets.ViewSet):
    """ Displays all the playlist
    """
    def add_playlist(self, request):
        serializer = PlaylistSerializer(data=self.request.data)
        import pdb;pdb.set_trace()
