from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^artists$', views.artists, name='artists'),
    url(r'^artist/(?P<name>(A-Za-z)+)$', views.artistdetails, name="artistdetails"),
]