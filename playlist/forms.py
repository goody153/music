from django import forms

from playlist.models import Song, Playlist


class PlaylistForm(forms.ModelForm):
    """Form for creating playlist
    """

    class Meta:
        model = Playlist
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        """ playlist needs an owner
        """
        self.user = kwargs.pop('user', None)
        return super(PlaylistForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """ overridden save
        """
        instance = super(PlaylistForm, self).save(commit=False)
        instance.user = self.user
        instance.save()
        return instance


class SongForm(forms.ModelForm):
    """Form for adding song on a playlist
    """

    class Meta:
        model = Song
        fields = ['title', 'link']

    def __init__(self, *args, **kwargs):
        """ User and playlist are used for creation of song
        """
        self.user = kwargs.pop('user', None)
        self.playlist = kwargs.pop('playlist', None)

        return super(SongForm, self).__init__(*args, **kwargs)

    def clean_link(self):
        """ check youtube id length
        """
        if len(self.cleaned_data['link']) < 11:
            raise forms.ValidationError("Youtube id length is invalid.")
        return self.cleaned_data['link']

    def save(self, commit=True):
        """ Song creation needs user and playlist 
        """
        instance = super(SongForm, self).save(commit=False)
        #checks if self.user and self.playlist exists to determine if it's a creation process
        if self.user and self.playlist:
            instance.user = self.user
            instance.playlist = self.playlist
        #when updating a song it only uses the instance passed
        else:
            instance.user = self.instance.user
            instance.playlist = self.instance.playlist
        instance.save()
        return instance