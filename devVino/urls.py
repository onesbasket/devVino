from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^list/', include('listSummary.urls')),
    # Examples:
    # url(r'^$', 'devVino.views.home', name='home'),
    # url(r'^devVino/', include('devVino.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    # Uncomment the next line to enable the admin:
   # url(r'^list/', include('listSummary.urls')),
)
