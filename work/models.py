from django.db import models


class Room(models.Model):
    type = models.CharField(max_length=30) # for example, deluxe, double, single etc..
    price = models.IntegerField(max_length=30)
    space = models.IntegerField(max_length=10)
    numberOfPeople = models.IntegerField(max_length=10)
    numberOfRoom = models.IntegerField(max_length=10)


class Hall(models.Model):
    type = models.CharField(max_length=30)
    persons = models.IntegerField(max_length=10)


class RoomReservation(models.Model):
    reserveID = models.AutoField(primary_key=True)

    # Personal Data
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    # Stay Data
    room = models.ForeignKey('Room')
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    numberOfPeople = models.IntegerField()
    payment = models.CharField(max_length=30)
    request = models.TextField()


class BanquetReservation(models.Model):
    reserveID = models.AutoField(primary_key=True)

    # Personal Data
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    # Hall Data
    hall = models.ForeignKey('Hall')
    reservationDateTime = models.DateTimeField()
    minimumNumberOfPeople = models.IntegerField(max_length=15)
    maximumNumberOfPeople = models.IntegerField(max_length=15)
    request = models.TextField()


class RestaurantReservation(models.Model):
    reserveID = models.AutoField(primary_key=True)

    # Personal Data
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    # Restaurant Data
    reservationDateTime = models.DateTimeField()
    numberOfPeople = models.IntegerField()
    request = models.TextField()


class Article(models.Model):
    articleID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()


class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=32)
    content = models.TextField()
    article = models.ForeignKey('Article')

