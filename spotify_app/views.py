from django.http import HttpResponse
import requests
from django.shortcuts import render
from django.views import generic

from spotify_app.models import Playlist
import json


# Create your views here.
url = 'https://api.spotify.com/v1/browse/featured-playlists'
#OAuthKey = "BQDxndovNrKJdfO-0HQWkRg00WQHIMYENGAZvp3wGAX-1GpDDZttXrxSpQwyqjWB2xl_Pj8vEAFSJKcqvQKiVjnSfRUzRe0UjKMy24OEjaosmd5CwL3Dd66ox7nehvrMcWYuIgjtfT7PtJpn0NOUO1hqnpLpirO-cLjDJNczfUJd55mKjjH3G1pAw5MKoa5-z_c"


def get_oauthKey():
    key =  requests.get("https://pst.klgrth.io/paste/ksv6q/raw").text
    return key
def get_playlists(request: object) -> object:
    response = requests.get(url, headers={"Authorization": "Bearer " + get_oauthKey()})
    if response.status_code != 401:
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
    print("Authorization:" "Bearer " + get_oauthKey())
    response = requests.get(url, headers={"Authorization": "Bearer " + get_oauthKey()})
    if response.status_code != 401:
        data = response.json()["playlists"]["items"]
        for playlist in data:
            if not Playlist.objects.filter(name=playlist["name"]).exists():
                Playlist.objects.create(name=playlist["name"], owner=playlist["owner"]["display_name"],
                                        isCollaborative=playlist["collaborative"], description=playlist["description"],
                                        url=playlist["external_urls"]["spotify"])
    else: print(response)

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
