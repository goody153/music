import httplib2
import os
import sys
import re

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

from django.conf import settings

class Youtube(object):
    """ This is a class that accepts a video id and returns essential data
    """

    image_url = None
    data = None

    # for authentication purposes
    args = argparser.parse_args('--auth_host_name 8000 --logging_level INFO'.split())
    
    # PLEASE DELETE THIS BLOCK ONCE DONE WITH DEBUGGING
    #--------------------------------------------------
    """ If you are authenticating from the command line and your browser doesn't support
        Javascript, you may want to add the argument --noauth_local_webserver:
    """
    # argparser.parse_args('--auth_host_name localhost --logging_level INFO --noauth_local_webserver'.split())
    #--------------------------------------------------

    def authenticate_yt(self):
        # Authorize the request and store authorization credentials.
        flow = flow_from_clientsecrets(settings.CLIENT_SECRETS_FILE, scope=settings.YOUTUBE_READ_WRITE_SSL_SCOPE,
            message=settings.MISSING_CLIENT_SECRETS_MESSAGE)

        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, storage, self.args)

        # Trusted testers can download this discovery document from the developers page
        # and it should be in the same directory with the code.
        return build(settings.API_SERVICE_NAME, settings.API_VERSION,
            http=credentials.authorize(httplib2.Http()))

    def remove_empty_kwargs(self, **kwargs):
        # Remove keyword arguments that are not set
        good_kwargs = {}
        if kwargs is not None:
            for key, value in kwargs.items():
                if value:
                    good_kwargs[key] = value
        return good_kwargs

    def videos_list_by_id(self, service, **kwargs):
        # returns all the data of a given id, also sets the global data
        kwargs = self.remove_empty_kwargs(**kwargs)
        results = service.videos().list(
          **kwargs
        ).execute()

        self.data = results
        return self.data

    def set_data(self, code):
        # this will set the current video
        data = self.videos_list_by_id(self.authenticate_yt(),
                        part="snippet,contentDetails",
                        id=code)
        if data:
            return data
        return None

    def get_image_url(self):
        # returns the image url
        item = self.data['items'][0]['snippet']['thumbnails']['default']['url']
        if item:
            return item
        return None

    def get_title(self):
        # returns the title
        item = self.data['items'][0]['snippet']['localized']['title']
        if item:
            return item
        return None

    def get_description(self):
        # returns the description
        item = self.data['items'][0]['snippet']['description']
        if item:
            return item
        return None

    def _convert_duration(self, dur):
        # converts the string to int
        return int(''.join([x for x in dur if x.isdigit()]))

    def get_time_code(self):
        # returns the time code in this format: PTHMS (string)
        duration = self.data['items'][0]['contentDetails']['duration']
        if duration:
            return duration
        return None

    def get_duration(self, duration):
        # accepts a string time code and returns time in seconds
        if duration:
            # match the duration to the regex
            match = re.match('PT(\d+H)?(\d+M)?(\d+S)?', duration).groups()
            hours = self._convert_duration(match[0]) if match[0] else 0
            minutes = self._convert_duration(match[1]) if match[1] else 0
            seconds = self._convert_duration(match[2]) if match[2] else 0
            return hours * 3600 + minutes * 60 + seconds
        return None





