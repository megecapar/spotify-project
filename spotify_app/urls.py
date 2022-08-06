from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path("update_playlists/", PlaylistUpdateView.as_view(), name="update_playlists"),
    path("playlists/", PlaylistView.as_view(), name="playlist"),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),

]
