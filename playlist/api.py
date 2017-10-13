from playlist.models import Playlist, Song
from playlist.serializers import PlaylistSerializer, SongSerializer
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
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SongViewSet(viewsets.ViewSet):
    """ Edit song from playlist
    """

    def song_update(self, *args, **kwargs):
        song = get_object_or_404(Song, id=kwargs['song_id'])
        serializer = SongSerializer(song, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

