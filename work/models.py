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

# Create your models here.
