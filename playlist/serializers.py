from rest_framework import serializers
from playlist.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    get_thumb_url = serializers.ReadOnlyField()

    class Meta:
        model = Playlist
        fields = ('title','user_email','get_thumb_url',)

    def get_user_email(self, obj):
        return obj.user.email