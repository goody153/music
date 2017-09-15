from django.conf.urls import url

from .views import UserLoginView, DashboardView, UserLogoutView, RegisterView,UserProfile

urlpatterns = [
    url(r'^login/$', UserLoginView.as_view(), name='user_login'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^logout/$', UserLogoutView.as_view(), name="user_logout"),
    url(r'^registration/$', RegisterView.as_view(), name='register'),
    url(r'^profile/$', UserProfile.as_view(), name="user_profile"),
]