from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from blog.models import *
# Create your views here.

def home(request):
    return render_to_response("blog/home.html")


def artists(request):
    artists = Artist.objects.all()
    return render_to_response("blog/artists.html", {"artists": artists})


def artistdetails(request, name):
    a=3