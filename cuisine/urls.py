from django.conf.urls import patterns, url


urlpatterns = patterns(
    'cuisine.views',
    url(r'^restaurant/$', 'restaurant_list', name='restaurant_list'),
    url(r'^restaurant/(?P<pk>[0-9]+)$', 'restaurant_detail', name='restaurant_detail'),
    )