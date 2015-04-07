from django.conf.urls import patterns, url


urlpatterns = patterns('cuisine.views',
                       url('^$', 'ViewAll'),
                       )