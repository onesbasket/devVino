# -*- coding: cp932 -*-
from django.shortcuts import render_to_response

from Consolidate.models import Item, Itemmaster
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
#Purpose:Pagenation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Purpose:Keyword search
import re
from django.db.models import Q
from django import forms
import operator
from django.db import connection
from django.utils.encoding import smart_str, smart_unicode

# �����t�H�[��
class SearchForm(forms.Form):
    q = forms.CharField(label="keyword")

def index(request):

    form = SearchForm() # �񑩔��t�H�[��
    latest_poll_list = Item.objects.all().select_related()
    paginator = Paginator(latest_poll_list, 100)# Show 25 contacts per page
    page = request.GET.get('page')
    try:
        latest_poll = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_poll = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_poll = paginator.page(paginator.num_pages)
    return render_to_response('Consolidate/index.html',
                              {'latest_poll_list': latest_poll,#���X�g�\��
                                'form': form,#�����t�H�[���\��
                               })

def detail(request, Item_id):
    p = get_object_or_404(Item, pk=Item_id)
    SourceItem  = Item.objects.get(pk=Item_id)
    idFilter = None#SourceItem.idProductNameCluster
    idFilterKana = None#SourceItem.idProductNameKanaCluster
    idFilterNonSpace = None#SourceItem.idProductNameNonspaceCluster
    #if idFilter is None:
    #   return render_to_response('Consolidate/detail.html', {'latest_poll_list': "None",'check':idFilter}) 
    query1 = Item.objects.filter(itembk__id__contains='1')#aaafilter(idProductNameCluster=idFilter)
    query2 = Item.objects.filter(idProductNameKanaCluster=idFilterKana)
    query3 = Item.objects.filter(idProductNameNonspaceCluster=idFilterNonSpace)
    DaieiTable1 = query1.filter(nameShopChain="DaieiTable")
    IyTable1 = query1.filter(nameShopChain="IyTable")
    DaieiTable2 = query2.filter(nameShopChain="DaieiTable")
    IyTable2 = query2.filter(nameShopChain="IyTable")
    DaieiTable3 = query3.filter(nameShopChain="DaieiTable")
    IyTable3 = query3.filter(nameShopChain="IyTable")
    return render_to_response('Consolidate/detail.html', {'DaieiTable1': DaieiTable1,'IyTable1': IyTable1,'DaieiTable2': DaieiTable2,'IyTable2': IyTable2,'DaieiTable3': DaieiTable3,'IyTable': IyTable3,'SourceItem': SourceItem,'check':idFilter})

def idProductNameCluster(request, Cluster_id):
    if Cluster_id == "None":
        query = Item.objects.filter(idProductNameCluster=None)[:500]
    else:
        query = Item.objects.filter(idProductNameCluster=Cluster_id)

    paginator = Paginator(query, 100)# Show 25 contacts per page
    page = request.GET.get('page')
    try:
        latest_poll = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_poll = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_poll = paginator.page(paginator.num_pages)
    
    return render_to_response('Consolidate/idProductNameCluster.html', {'Cluster': latest_poll})



#query search
# �󔒕����̍폜
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    query_string = query_string.replace(u'�@', ' ')
    query_string = query_string.replace(u'�A', ' ')
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

# �����N�G���쐬
def get_query(query_string):
    query = None 
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None 
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query



# �u���O�\��
def search(request):
    form = SearchForm(request.GET) # GET �f�[�^�̑����t�H�[��
    if form.is_valid(): # �o���f�[�V������ʂ���
        query_string = request.GET['q']
        found_entries=Item.objects.filter(reduce(operator.or_, [Q(productName__contains=keyword.encode('utf-8')) for keyword in query_string.split(' ')])).order_by('idProductName')
        qs = smart_str(found_entries.query)
        return render_to_response('Consolidate/searchresult.html',
                                  {'latest_poll_list': found_entries,#���X�g�\��
                                   'qs': qs,
                                   'form': form
                                   })
