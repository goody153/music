from django import forms

from playlist.models import Song, Playlist


class PlaylistForm(forms.ModelForm):
    """To Add/Edit Playlist
    """

    class Meta:
        model = Playlist
        fields = ['title', 'description']


class SongForm(forms.ModelForm):
    """To Add/Edit Song
    """

    class Meta:
        model = Song
        fields = ['title', 'link']

    def __init__(self, *args, **kwargs):
        #needed to create song
        self.user = kwargs.pop('user', None)
        self.playlist = kwargs.pop('playlist', None)

        return super(SongForm, self).__init__(*args, **kwargs)

    def save(self):
        super(SongForm, self).save(commit=False)
        song = Song.objects.create(
            user=self.user,
            playlist=self.playlist,
            title=self.cleaned_data['title'],
            link=self.cleaned_data['link']
        )

        return song


class UpdateSongForm(forms.ModelForm):
    """To Add/Edit Song
    """

    class Meta:
        model = Song
        fields = ['title', 'link']
