from django.conf.urls import url

from .views import UserLogin, Dashboard, UserLogout, RegisterView

urlpatterns = [
    url(r'^login/$', UserLogin.as_view(), name='user_login'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^logout/$', UserLogout.as_view(), name="user_logout"),
    url(r'^registration/$', RegisterView.as_view(), name='register'),
]