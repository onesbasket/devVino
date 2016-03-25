from __future__ import absolute_import  # Python 2 only

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from jinja2 import Environment

from devVino.form import KakikomiForm

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env

def kakikomi(request):
	f = KakikomiForm()
	return HttpResponse(f)

def user_name(request):
    print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print request.GET.get('lowPrice')
    return "aaa"#request.GET.get('lowPrice')

