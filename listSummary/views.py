# coding: utf-8

#  Create your views here.
from listSummary.models import vino_transferSummary,tagCountry, tagRegion, tagGrape, vino_transferDetail,  vino_transferSummary_Year

#RequestContext
from django.template import RequestContext

#Purpose:Pagenation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.shortcuts import render_to_response, get_object_or_404

from devVino.processRequestGet import test
from devVino.form import KakikomiForm, selectionListForm,shopFilterForm

from django.db.models import Avg, Max, Min

from django.db.models import Q

from django.http import HttpResponse, HttpResponseNotAllowed

import json

def truncate_session(request):
    try:
        del request.session['mykey']
        print "truncate!!!!"
    except KeyError:
        pass
    return HttpResponse("clear")

def update_session(request):
    if not 'mykey' in request.session:
       request.session['mykey']=[]
    listItemIds = request.session['mykey']
    if 'itemid' in request.POST:
        itemid = request.POST['itemid']
        print listItemIds
        print itemid
        listItemIds.append(itemid)
        request.session['mykey'] = listItemIds

    queryDetail = vino_transferDetail.objects.filter(summaryId__in=request.session['mykey']).order_by('itemPrice')
    querySummary = vino_transferSummary.objects.values('kanaName', 'id').filter(id__in=request.session['mykey'])
    listWINE = []
    dictShop = {}
    for Item in queryDetail:
        if dictShop.has_key(Item.shopCode):
            dictShop.update({Item.shopCode:{"shopName": Item.shopName,"bottle":dictShop[Item.shopCode]["bottle"]+1,"sumPrice": dictShop[Item.shopCode]["sumPrice"]+Item.itemPrice }})
        else:
            dictShop.update({Item.shopCode:{"shopName": Item.shopName,"bottle": 1,"sumPrice": Item.itemPrice }})

        print dictShop[Item.shopCode]

    for Item in querySummary:
        print Item['kanaName']
        listWINE.append('{"selectedName": "' + Item['kanaName'] + '","selectedId":"' + str(Item['id']) + '"}')
        print "--------------------ree"
    print "--"
    print json.dumps(dictShop)
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST',])
    listJSON = '{"shops":'+ json.dumps(dictShop) +',"wines":['+",".join(listWINE)+']}'
    print listJSON
    return HttpResponse(listJSON)


def detailInfo(request, Item_id):
    querySummary = vino_transferSummary.objects.values('id', 'kanaName', 'itemPrice', 'reviewAvarage', 'reviewCount', 'imageUrl').filter(id=Item_id).prefetch_related("vino_transfersummary_tastetype_set").prefetch_related("vino_transfersummary_year_set")
    queryDetail = vino_transferDetail.objects.filter(summaryId=Item_id).order_by('itemPrice')
    aggression =queryDetail.aggregate(Max('itemPrice'), Min('itemPrice'))
    print "------------------"
    print len(queryDetail)
    context_instance =  {'querySummary': querySummary,
                         'queryDetail': queryDetail,
                         'aggression': aggression}

    return render(request,'detail.html',context_instance,)#,

def listSummary(request):
    #f = test(request)

    f = KakikomiForm(request.GET)
    print f.is_valid()
    cleanData = f.cleaned_data

    shopfilterform = shopFilterForm(request.GET)
    print shopfilterform.is_valid()
    cleanDataShopFilter = shopfilterform.cleaned_data

    selectQuery = vino_transferSummary.objects.values('id', 'kanaName', 'itemPrice', 'reviewAvarage', 'reviewCount', 'imageUrl','itemPriceDiscount').prefetch_related("vino_transfersummary_tastetype_set").prefetch_related("vino_transfersummary_year_set").prefetch_related("vino_transfersummary_shopid_set")
    if cleanData.get('lowPrice') and cleanData.get('highPrice'):
        getLowPrice = float(cleanData.get('lowPrice'))
        getHighPrice = float(cleanData.get('highPrice'))
        selectQuery = selectQuery.filter(itemPrice__gte= getLowPrice, itemPrice__lte= getHighPrice)
    elif cleanData.get('lowPrice'):
        getLowPrice = float(cleanData.get('lowPrice'))
        selectQuery = selectQuery.filter(itemPrice__gte= getLowPrice)
    elif cleanData.get('highPrice'):
        getHighPrice = float(cleanData.get('highPrice'))
        selectQuery = selectQuery.filter(itemPrice__lte= getHighPrice)

    if cleanData.get('lowYears') and cleanData.get('highYears'):
        getLowYears = cleanData.get('lowYears')
        getHighYears = cleanData.get('highYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year__gte= getLowYears, vino_transfersummary_year__year__lte= getHighYears)
    elif cleanData.get('lowYears'):
        getLowYears = cleanData.get('lowYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year__gte= getLowYears)
    elif cleanData.get('highYears'):
        getHighYears = cleanData.get('highYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year__lte= getHighYears)


    if cleanData.get('exactYears'):
        getYears = cleanData.get('exactYears')
        selectQuery = selectQuery.filter(vino_transfersummary_year__year= getYears)

    if cleanData.get('lowVolume'):
        getLowPrice = cleanData.get('lowVolume')

    if cleanData.get('highVolume'):
        getHighPrice = cleanData.get('highVolume')


    if cleanData.get('reviewAvarage'):
        getReviewAvarage = cleanData.get('reviewAvarage')
        selectQuery = selectQuery.filter(reviewAvarage__gt= getReviewAvarage)

    if cleanData.get('discount'):
        getReviewAvarage = cleanData.get('discount')
        selectQuery = selectQuery.filter(itemPriceDiscount__gt= getReviewAvarage)

    if cleanData.get('reviewCount'):
        getReviewCount = cleanData.get('reviewCount')

    if cleanData.get('tasteType'):
        getTasteType = cleanData.get('tasteType')
        selectQuery = selectQuery.filter(vino_transfersummary_tastetype__tasteType=getTasteType)


    if cleanDataShopFilter.get('shopFilter') and request.session.has_key('mykey'):
        getShopFileter = request.GET.getlist('shopFilter')
        if len(getShopFileter)==1 and  getShopFileter[0] == "on":
            queryShopCode = vino_transferDetail.objects.values_list('shopCode').filter(summaryId__in=request.session['mykey'])
        else:
            queryShopCode = getShopFileter
        selectQuery = selectQuery.filter(vino_transfersummary_shopid__shop__in=queryShopCode)


    if cleanData.get('search'):
        searchWord = cleanData.get('search')
        print searchWord
        selectQuery = selectQuery.filter(Q(kanaName__contains=searchWord))





    #values_listで値渡しすぎるとSQLエラーになるので、あえて遅くなりやすいけどSQLをネストさせてる。
    f2 = selectionListForm(request.GET)
    f2.fields['grapeIds'].queryset = tagGrape.objects.distinct().filter(vino_transfersummary__id__in=selectQuery.values_list("id", flat=True))
    f2.fields['regionIds'].queryset = tagRegion.objects.distinct().filter(vino_transfersummary__id__in=selectQuery.values_list("id", flat=True))
    f2.fields['countryIds'].queryset = tagCountry.objects.distinct().filter(vino_transfersummary__id__in=selectQuery.values_list("id", flat=True))
    print f2.is_valid()


    if request.GET.getlist('grapeIds'):
        getGrapeIds = request.GET.getlist('grapeIds')
        selectQuery = selectQuery.filter(tagGrape__in=getGrapeIds)


    if request.GET.getlist('countryIds'):
        getCountryIds = request.GET.getlist('countryIds')
        print "=======================", getCountryIds
        selectQuery = selectQuery.filter(tagCountry__in=getCountryIds)

    if request.GET.getlist('regionIds'):
        getRegionIds = request.GET.getlist('regionIds')
        selectQuery = selectQuery.filter(tagRegion__in=getRegionIds)


    #print "999999999999999999999999"
    #print f2
    #print cleanData
    #for testes in f2:
    #    print "&&&&&&&&&&&&&&&&"
    #    print testes.field
    #print "f2"
    #print f2.is_valid()

    if request.GET.get('sort'):
        sort = request.GET.get('sort')
        selectQuery = selectQuery.order_by(sort)



    paginator = Paginator(selectQuery, 25)# Show 25 contacts per page
    page = request.GET.get('page')
    try:
        responseData = paginator.page(page)
        numPage = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        responseData = paginator.page(1)
        numPage = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        responseData = paginator.page(paginator.num_pages)
        numPage = paginator.num_pages

    lowNumCount = responseData[0]['id']
    print "aaa", lowNumCount
    highNumCount = responseData[-1]['id']
    print "aaa2", highNumCount

    selectCountryQuerys = tagCountry.objects.filter(vino_transfersummary__id__gte=lowNumCount, vino_transfersummary__id__lte=highNumCount).values('vino_transfersummary__id',"name","engName")
    dictCountry = {}
    dictCountryEng = {}
    for selectCountryQuery in selectCountryQuerys:
        dictCountry[selectCountryQuery["vino_transfersummary__id"]] = selectCountryQuery["name"]
        dictCountryEng[selectCountryQuery["vino_transfersummary__id"]] = selectCountryQuery["engName"]

    selectGrapeQuerys = tagGrape.objects.filter(vino_transfersummary__id__gte=lowNumCount, vino_transfersummary__id__lte=highNumCount).values('vino_transfersummary__id',"name")
    dictGrape = {}
    for selectGrapeQuery in selectGrapeQuerys:
        if dictGrape.has_key(selectGrapeQuery["vino_transfersummary__id"]):
            dictGrape[selectGrapeQuery["vino_transfersummary__id"]] = dictGrape[selectGrapeQuery["vino_transfersummary__id"]] +"/"+ selectGrapeQuery["name"]
        else:
            dictGrape[selectGrapeQuery["vino_transfersummary__id"]] = selectGrapeQuery["name"]

    selectRegionQuerys = tagRegion.objects.filter(vino_transfersummary__id__gte=lowNumCount, vino_transfersummary__id__lte=highNumCount).values('vino_transfersummary__id',"name")
    dictRegion = {}
    for selectRegionQuery in selectRegionQuerys:
        if dictRegion.has_key(selectRegionQuery["vino_transfersummary__id"]):
            dictRegion[selectRegionQuery["vino_transfersummary__id"]] = dictRegion[selectRegionQuery["vino_transfersummary__id"]] +"/"+ selectRegionQuery["name"]
        else:
            dictRegion[selectRegionQuery["vino_transfersummary__id"]] = selectRegionQuery["name"]



    print "------------------aaaaaa---------------", RequestContext(request)
    request_context = RequestContext(request)
    request_context.push({"my_name": "Adrian"})


    context_instance =  {'responseData': responseData,
                               'country': dictCountry,
                               'engCountry': dictCountryEng,
                               'grape': dictGrape,
                               'region': dictRegion,
                               'forms': f,
                               'forms2': f2,
                               'shopFilterForm': shopfilterform}
    print context_instance

    return render(request,'item_list.html',context_instance,)#,
                               #context_instance=RequestContext(request))