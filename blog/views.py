from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from blog.models import *

# Create your views here.

def home(request):
    return render_to_response("blog/home.html")


def artists(request):
    artists = Artist.objects.all()
    return render_to_response("blog/artists.html", {"artists": artists})


def artistCreate(request):
    if request.method == "GET":
        form = ArtistForm()
        return render(request, 'blog/artistcreate.html', {'form':form})
    elif request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect('/artists')


def artistdetails(request, id):
    artist = Artist.objects.get(pk=id)
    return render_to_response("blog/artistdetails.html", {"artist": artist})