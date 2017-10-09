from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework import status


class PlaylistViewSet(viewsets.ViewSet):
    """ Displays all the playlist
    """
    def add_playlist(self, request):
        serializer = PlaylistSerializer(data=self.request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
