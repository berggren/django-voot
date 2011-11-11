"""URLs for voot application."""

from django.conf.urls.defaults import *


urlpatterns = patterns('voot.views',
    url(r'^$', view='index', name='voot_index'),
)
