from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^review/', include('review.urls')),
    url(r'^$', include('cuisine.urls')),
    # Examples:
    # url(r'^$', 'restaurant.views.home', name='home'),
    # url(r'^restaurant/', include('restaurant.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
