from django.http import HttpResponse
import requests
from django.shortcuts import render
from django.views import generic

from spotify_app.models import Playlist
import json


# Create your views here.
url = 'https://api.spotify.com/v1/browse/featured-playlists'
OAuthKey = "BQA-Nq5F96VYO8Z3eKuNP-ftT4dYE_zHeet0NS4GVDGFfaf4oTt9U2AONAiLpGhlHejTf4r2KYMCvezGhKQ2XfwNrjbdaPG8MlvGtIPlt3yHk7FRECzc1b7weXYKWrNM22nDJRLi98KLelu3wGxbariy9FjHvManFXWTQSG4a3sMgM5_XY3Pd44kDAOB4NgcI2A"


def get_playlists(request: object) -> object:
    response = requests.get(url, headers={"Authorization": "Bearer " + OAuthKey})
    data = response.json()["playlists"]["items"]
    for playlist in data:
        if not Playlist.objects.filter(name=playlist["name"]).exists():
            Playlist.objects.create(name=playlist["name"],owner=playlist["owner"]["display_name"],isCollaborative=playlist["collaborative"],description=playlist["description"],url=playlist["external_urls"]["spotify"])
    print(Playlist.objects.all())
    return render(request, "playlists.html", {"response": Playlist.objects.all()})


class PlaylistView(generic.ListView):

    model = Playlist
    template_name = "playlists.html"
    context_object_name = 'playlists'


class PlaylistUpdateView(generic.ListView):
    response = requests.get(url, headers={"Authorization": "Bearer " + OAuthKey})
    data = response.json()["playlists"]["items"]
    for playlist in data:
        if not Playlist.objects.filter(name=playlist["name"]).exists():
            Playlist.objects.create(name=playlist["name"], owner=playlist["owner"]["display_name"],
                                    isCollaborative=playlist["collaborative"], description=playlist["description"],
                                    url=playlist["external_urls"]["spotify"])


    model = Playlist
    template_name = "playlists.html"
    context_object_name = 'playlists'


class PlaylistDetailView(generic.DetailView):

    model = Playlist
    template_name = 'playlist-detail.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


def index(request):
    return render(request, "index.html")
