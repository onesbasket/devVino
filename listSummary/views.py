# Create your views here.
from listSummary.models import vino_transferSummary,  vino_transferSummary_Year

#RequestContext
from django.template import RequestContext

#Purpose:Pagenation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response, get_object_or_404

def listSummary(request):
    selectQuery = vino_transferSummary.objects.select_related().all().prefetch_related("vino_transfersummary_tastetype_set").prefetch_related("vino_transfersummary_year_set")
    if request.GET.get('lowPrice') and request.GET.get('highPrice'):
        getLowPrice = float(request.GET.get('lowPrice'))
        getHighPrice = float(request.GET.get('highPrice'))
        selectQuery = selectQuery.filter(itemPrice__gte= getLowPrice, itemPrice__lte= getHighPrice)
    elif request.GET.get('lowPrice'):
        getLowPrice = float(request.GET.get('lowPrice'))
        selectQuery = selectQuery.filter(itemPrice__gte= getLowPrice)
    elif request.GET.get('highPrice'):
        getHighPrice = float(request.GET.get('highPrice'))
        selectQuery = selectQuery.filter(itemPrice__lte= getHighPrice)

    if request.GET.get('lowYears') and request.GET.get('highYears'):
        getLowYears = request.GET.get('lowYears')
        getHighYears = request.GET.get('highYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year__gte= getLowYears, vino_transfersummary_year__year__lte= getHighYears)
    elif request.GET.get('lowYears'):
        getLowYears = request.GET.get('lowYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year__gte= getLowYears)
    elif request.GET.get('highYears'):
        getHighYears = request.GET.get('highYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year__lte= getHighYears)


    if request.GET.get('lowVolume'):
        getLowPrice = request.GET.get('lowVolume')

    if request.GET.get('highVolume'):
        getHighPrice = request.GET.get('highVolume')


    if request.GET.get('reviewAvarage'):
        getReviewAvarage = request.GET.get('reviewAvarage')
        selectQuery = selectQuery.filter(reviewAvarage__gt= getReviewAvarage)

    if request.GET.get('reviewCount'):
        getReviewCount = request.GET.get('reviewCount')

    if request.GET.get('tasteType'):
        getTasteType = request.GET.get('tasteType')
        selectQuery = selectQuery.filter(vino_transfersummary_tastetype__tasteType=getTasteType)

    if request.GET.get('countryIds'):
        getCountryIds = request.GET.get('countryIds')
        selectQuery = selectQuery.filter(tagCountry__exact=getCountryIds)

    if request.GET.get('regionIds'):
        getRegionIds = request.GET.get('regionIds')
        selectQuery = selectQuery.filter(tagRegion__exact=getRegionIds)

    if request.GET.get('grapeIds'):
        getGrapeIds = request.GET.get('grapeIds')
        selectQuery = selectQuery.filter(tagGrape__exact=getGrapeIds)

    paginator = Paginator(selectQuery, 25)# Show 25 contacts per page
    page = request.GET.get('page')
    try:
        responseData = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        responseData = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        responseData = paginator.page(paginator.num_pages)
    return render_to_response('item_list.html',
                              {'responseData': responseData,
                               },
                               context_instance=RequestContext(request))