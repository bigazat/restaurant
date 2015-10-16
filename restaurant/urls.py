from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'cuisine.views.view_html'),
    url(r'^cuisine/', include('cuisine.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
