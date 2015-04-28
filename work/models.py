from django.db import models

class Room(models.Model):
    type = models.CharField(max_length=30) # for example, deluxe, double, single etc..
    price = models.IntegerField(max_length=30)

class Reservation(models.Model):
    reserveID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    room = models.ForeignKey('Room')
    checkInDate = models.CharField(max_length=32)
    checkOutDate = models.CharField(max_length=32)
    phoneNumber = models.CharField(max_length=32)
    numberOfPeople = models.IntegerField()

class Article(models.Model):
    articleID = models.AutuField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()

class Content(models.Model):
    name = models.CharField(max_length=30)
    email = models.emailField()
    content = models.TextField()
    article = models.ForeignKey('Article')


# Create your models here.
