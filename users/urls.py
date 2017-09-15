from django.conf.urls import url

from .views import UserLogin, Dashboard, UserLogout

urlpatterns = [
    url(r'^login/$', UserLogin.as_view(), name='user_login'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^logout/$', UserLogout.as_view(), name="user_logout")
]