from django.db import models


class Room(models.Model):
    type = models.CharField(max_length=30) # for example, deluxe, double, single etc..
    price = models.IntegerField(max_length=30)
    space = models.IntegerField(max_length=10)
    numberOfPeople = models.IntegerField(max_length=10)
    numberOfRoom = models.IntegerField(max_length=10)

    def __str__(self):
        return '%s' % self.type


class Hall(models.Model):
    type = models.CharField(max_length=30)
    minimumNumberOfPeople = models.IntegerField(max_length=15)
    maximumNumberOfPeople = models.IntegerField(max_length=15)

    def __str__(self):
        return '%s' % self.type


class RoomReservation(models.Model):
    reserveID = models.AutoField(primary_key=True)

    # Personal Data
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    # Stay Data
    room = models.ForeignKey('Room', verbose_name="Room")
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    numberOfPeople = models.IntegerField()
    payment = models.CharField(max_length=30)
    request = models.TextField(blank=True, null=True)


class BanquetReservation(models.Model):
    reserveID = models.AutoField(primary_key=True)

    # Personal Data
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    # Hall Data
    hall = models.ForeignKey('Hall', verbose_name="Hall")
    reservationDate = models.DateField()
    reservationTime = models.CharField(max_length=30)
    numberOfPeople = models.IntegerField()
    request = models.TextField()


class RestaurantReservation(models.Model):
    reserveID = models.AutoField(primary_key=True)

    # Personal Data
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    # Restaurant Data
    reservationDate = models.DateField()
    reservationTime = models.CharField(max_length=30)
    numberOfPeople = models.IntegerField()
    request = models.TextField()


class Article(models.Model):
    articleID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(editable=False, auto_now_add=True)
    #category = models.ListField()

class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=32)
    content = models.TextField()
    article = models.ForeignKey('Article')
    date = models.DateTimeField(editable=False, auto_now_add=True)

