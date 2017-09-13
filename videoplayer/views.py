from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainTemplateview(TemplateView):
    """This is the main template for viewing videos
    """
    template_name = "videoplayer/swiftmusic.html"

    def get(self, *args, **kwargs):
        
        # this date will come from the playlist module
        songs = ['0Vf1TpucUss','QH2-TGUlwu4', 'e3cHO_Ud86Y']

        return render(self.request, self.template_name, {
            'songs': songs,
            }) 