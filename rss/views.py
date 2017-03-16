from django.shortcuts import render, render_to_response
from rss.models import Post

# Create your views here.
def home(request):

    posts = reversed(Post.objects.all())
    context = {
        'posts':posts
    }
    return render_to_response("rss/home.html", context)