from django.db import models
from django.forms import ModelForm
# Create your models here.
class Artist(models.Model):
    name = models.CharField("artist", max_length=50)
    year_formed = models.PositiveIntegerField()
    image = models.ImageField(upload_to='artist_img')

    def __str__(self):
        return str(self.id) +" "+ self.name

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'year_formed', 'image']

class Album(models.Model):
    name = models.CharField("album", max_length=50)
    artist = models.ForeignKey(Artist)