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
        self.user = kwargs.pop('user', None)
        self.playlist = kwargs.pop('playlist', None)
        return super(SongForm, self).__init__(*args, **kwargs)

    def save(self):
        # checks if save is supposed to update or create 
        if self.instance.id:
            Song.objects.filter(id=self.instance.id).update(
                title=self.cleaned_data['title'],
                link=self.cleaned_data['link'],
            )
            return
        Song.objects.create(
            title=self.cleaned_data['title'],
            link=self.cleaned_data['link'],
            playlist=self.playlist,
            user=self.user,
        )
        return