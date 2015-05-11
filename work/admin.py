from django.contrib import admin

# Models
from work.models import Room
from work.models import Hall
from work.models import RoomReservation
from work.models import BanquetReservation
from work.models import RestaurantReservation
from work.models import Article
from work.models import Comment


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'numberOfPeople')


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomReservation)
class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'room', 'checkInDate', 'checkOutDate', 'numberOfPeople', 'payment', 'request')


@admin.register(BanquetReservation)
class BanquetReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'hall', 'reservationDate', 'reservationTime', 'numberOfPeople', 'request')


@admin.register(RestaurantReservation)
class RestaurantReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'reservationDate', 'reservationTime', 'numberOfPeople', 'request')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

