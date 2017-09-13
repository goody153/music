from django.conf.urls import url, include

from .views import MainTemplateview


urlpatterns = [
    url(r'^', MainTemplateview.as_view(), name="main"),
]
