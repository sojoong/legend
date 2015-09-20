from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'legend.views.index'),
    url(r'^index','legend.views.index', name='index'),
    #url(r'^404\.html','legend.views.error')
    url(r'^room-list','legend.views.room_list', name='room-list'),
    url(r'^room-details','legend.views.room_details', name='room-detail'),
    url(r'^news', 'legend.views.news', name='news'),
    url(r'^write', 'legend.views.write', name='write'),

    url(r'^booking', 'legend.views.booking', name='booking'),
    url(r'^banquet-reservation', 'legend.views.banquet_reservation', name='banquet-reservation'),
    url(r'^restaurant-reservation', 'legend.views.restaurant_reservation', name='restaurant-reservation'),

    url(r'^contact', 'legend.views.contact', name='contact'),
    url(r'^fullwidth', 'legend.views.fullwidth', name='fullwidth'),
    url(r'^gallery', 'legend.views.gallery', name='gallery'),
    url(r'^single-news', 'legend.views.single_news', name='single-news'),

    url(r'^room-reservation-ok', 'legend.views.room_reservation_ok', name='room-reservation-ok'),

    url(r'^change_language/', 'legend.views.change_language'),
)
