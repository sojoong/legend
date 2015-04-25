from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'legend.views.index'),
    url(r'^index\.html','legend.views.index'),
    #url(r'^404\.html','legend.views.error')
    url(r'^room-list\.html','legend.views.room_list'),
    url(r'^room-details\.html','legend.views.room_details'),
    url(r'^news\.html', 'legend.views.news'),
    url(r'^booking\.html', 'legend.views.booking'),
    url(r'^contact\.html', 'legend.views.contact'),
    url(r'^fullwidth\.html', 'legend.views.fullwidth'),
    url(r'^gallery\.html', 'legend.views.gallery'),
    url(r'^single-news\.html', 'legend.views.single_news'),
)
