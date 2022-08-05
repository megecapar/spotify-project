from django.http import HttpResponse
import requests
from django.shortcuts import render
from django.views import generic

from spotify_app.models import Playlist
import json


# Create your views here.
url = 'https://api.spotify.com/v1/browse/featured-playlists'
OAuthKey = "BQBtXuGo3DPHNKKFTGVxhEtsveFvEB14__Yc5y6EdwZLtYQuS8QBob-gH3K7kKg8sfELmWLrhXCg59ehXtFcsusHR3lR1eRnguEAd1Ia4AtkoMqXdHLpoxDVAsXmELvx49bwg-oqPb3CLfB5wu66oXk-z5ZfDPSspWzeHFUNbbOC6762qHDCRtSJwfV6mvcFyBo"


def get_playlists(request):
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


class PlaylistDetailView(generic.DetailView):

    model = Playlist
    template_name = 'playlist-detail.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context