import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Xth(models.Model):
    def __unicode__(self):
        return self.number
    number = models.IntegerField()
    game = models.ForeignKey(Game)

class Game(models.Model):
    def __unicode__(self):
        return self.gameNumber
    number = models.ForeignKey(Xth)
    gameNumber = models.IntegerField()
    category = models.TextField(max_length=50)
    league = models.TextField(max_length=50)
    date = models.DateTimeField()
    odd = models.ForeignKey(Odd)
    
class Odd(models.Model):
    def __unicode__(self):
        return self.serviceProvider
    game = models.ForeignKey(Game)
    serviceProvider = models.TextField(max_length=50)
    winP = models.DecimalField()
    drawP = models.DecimalField()
    loseP = models.DecimalField()