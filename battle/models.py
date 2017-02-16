from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField("Player Name", max_length=20)

    def __str__(self):
        return str(self.id) +" "+ self.name

class WinRange(models.Model):
    number_of_win = models.PositiveIntegerField()
    number_of_lose = models.PositiveIntegerField()
    player = models.ForeignKey(Player)