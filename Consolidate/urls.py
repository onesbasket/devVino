from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from Consolidate.models import Item

urlpatterns = patterns('Consolidate.views',
    url(r'^$','index'),
    url(r'^search/$','listSummary'),
    url(r'^(?P<Item_id>\d+)/$', 'detail'),
    url(r'^idProductNameCluster\-(?P<Cluster_id>\w+)/$', 'idProductNameCluster'),
    url(r'^publishers/$', ListView.as_view(model=Item),
        ),)
#    url(r'^(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#)
