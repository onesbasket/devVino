from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from listSummary.models import vino_transferSummary

urlpatterns = patterns('listSummary.views',
    url(r'^$',ListView.as_view(model=vino_transferSummary),),
    url(r'^search/$','listSummary'),
    url(r'^detail/(?P<Item_id>\d+)/$', 'detailInfo'),
    url(r'^idProductNameCluster\-(?P<Cluster_id>\w+)/$', 'idProductNameCluster'),
        )
#    url(r'^(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#)
