from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField("artist", max_length=50)
    year_formed = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id) +" "+ self.name

class Album(models.Model):
    name = models.CharField("album", max_length=50)
    artist = models.ForeignKey(Artist)
