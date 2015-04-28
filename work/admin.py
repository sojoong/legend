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
    pass


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomReservation)
class RoomReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(BanquetReservation)
class BanquetReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantReservation)
class RestaurantReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

