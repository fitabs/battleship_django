from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^artists$', views.artists, name='artists'),
    url(r'^artists/(?P<id>\d+)$', views.artistdetails, name="artistdetails"),
    url(r'^artists/create$', views.artistCreate, name="artistdetails"),
]