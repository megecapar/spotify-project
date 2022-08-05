from django.urls import path
from .views import *

urlpatterns = [
    path("", get_playlists, name="home"),
    path("playlists/", PlaylistView.as_view(), name="playlist"),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),

]
