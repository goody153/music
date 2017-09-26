from django import forms

from playlist.models import Song, Playlist
from playlist.YoutubeApi import Youtube

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

    def clean_title(self):
        """ overriden so that there cannot be the same playlist name from a user
        """
        playlist = Playlist.objects.filter(
            title=self.cleaned_data['title'],
            user=self.user
        )
        if playlist.exists():
            raise forms.ValidationError(
                'You already have a playlist with the same name'
            )
        return self.cleaned_data['title']


class SongForm(Youtube, forms.ModelForm):
    """Form for adding song on a playlist
    """
    link = forms.CharField(max_length=60)

    class Meta:
        model = Song
        fields = ['link']

    def __init__(self, *args, **kwargs):
        """ User and playlist are used for creation of song
        """
        self.user = kwargs.pop('user', None)
        self.playlist = kwargs.pop('playlist', None)

        return super(SongForm, self).__init__(*args, **kwargs)

    def clean_link(self):
        """ check link validations
        """
        #check youtube id length validation
        if len(self.cleaned_data['link']) < 11:
            raise forms.ValidationError("Youtube id length is invalid.")
        #turns full url sent into proper youtube id needed
        url = self.cleaned_data['link']
        if '/v/' in url:
            url = url.split('/v/',1)[1]
        elif '/watch?v=' in url:
            url = url.split('/watch?v=',1)[1]
        elif '/watch?feature=player&v=' in url:
            url = url.split('/watch?feature=player&v=',1)[1]
        elif '/youtu.be/' in url:
            url = url.split('/youtu.be/',1)[1]
        elif '/embed/' in url:
            url = url.split('/embed/')[1]
        #to make it only takes 11 characters from the delimiter
        self.cleaned_data['link'] = url[:11]
        #check if song already exists
        song = Song.objects.filter(
            link=self.cleaned_data['link'],
            user=self.user,
            playlist=self.playlist,
            archive=False
            )
        if song.exists():
            raise forms.ValidationError("Song already exists on this playlist.")
        return self.cleaned_data['link']

    def save(self, commit=True):
        """ Song creation needs user and playlist 
        """
        song = super(SongForm, self).save(commit=False)
        # if self.user and self.playlist exists then it creates otherwise update
        song.user = self.user if self.user else self.instance.user
        song.playlist = self.playlist if self.playlist else self.instance.playlist
        yt_video = self.set_data(song.link)
        song.title = self.get_title()
        song.thumb_url = self.get_image_url()
        song.duration = self.get_duration(self.get_time_code())
        song.save()
        return song