import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Odd(models.Model):
    def __unicode__(self):
        return self.serviceProvider
    serviceProvider = models.TextField(max_length=50)
    winP = models.DecimalField(max_digits=10,decimal_places=5)
    drawP = models.DecimalField(max_digits=10,decimal_places=5)
    loseP = models.DecimalField(max_digits=10,decimal_places=5)

class Game(models.Model):
    def __unicode__(self):
        return self.gameNumber
    gameNumber = models.IntegerField()
    category = models.TextField(max_length=50)
    league = models.TextField(max_length=50)
    date = models.DateTimeField()
    odd = models.ForeignKey(Odd)

class Xth(models.Model):
    def __unicode__(self):
        return self.number
    number = models.IntegerField()
    game = models.ForeignKey(Game)