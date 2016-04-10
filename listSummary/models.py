# coding: utf-8
from django.db import models

# Create your models here.
class tagGrape(models.Model):
    class Meta:
        db_table= "tagGrape"
    name = models.CharField(null=True, db_column='name', max_length =100)

    def __unicode__(self):
        return self.name

class tagCountry(models.Model):
    class Meta:
        db_table= "tagCountry"
    name = models.CharField(null=True, db_column='name', max_length =100)
    engName = models.CharField(null=True, db_column='engName', max_length =100)

    def __unicode__(self):
        return self.name

class tagRegion(models.Model):
    class Meta:
        db_table= "tagRegion"
    name = models.CharField(null=True, db_column='name', max_length =100)

    def __unicode__(self):
        return self.name

class vino_transferSummary(models.Model):
    class Meta:
        db_table = "vino_transferSummary"

    kanaName = models.CharField(null=True, db_column='kanaName', max_length = 12000)
    itemPrice = models.FloatField(null=True, db_column='itemPrice')
    itemPriceDiscount = models.IntegerField(null=True, db_column='itemPriceDiscount')
    itemPriceDeviation = models.FloatField(null=True, db_column='itemPriceDeviation')
    itemPriceCoefficientVariation = models.FloatField(null=True, db_column='itemPriceCoefficientVariation')
    #years = models.ForeignKey(vino_transferSummary_Year.summaryId)
    #mlVolume = models.ForeignKey(vino_transferSummary_Mlvolume.summaryId)
    reviewAvarage = models.FloatField(null=True, db_column='reviewAvarage')
    reviewCount = models.IntegerField(null=True, db_column='reviewCount')
    #tasteType = models.ForeignKey(vino_transferSummary_TasteType.summaryId)
    countryIds = models.CharField(null=True, db_column='countryId', max_length = 1000)
    regionIds = models.CharField(null=True, db_column='regionId', max_length = 1000)
    grapeIds = models.CharField(null=True, db_column='grapeIds', max_length = 1000)
    imageUrl = models.CharField(null=True, db_column='imageUrl', max_length = 600)
    tagGrape = models.ManyToManyField(tagGrape)
    tagCountry  = models.ManyToManyField(tagCountry)
    tagRegion = models.ManyToManyField(tagRegion)

class vino_transferSummary_TasteType(models.Model):
    class Meta:
        db_table= "vino_transferSummary_TasteType"
    summaryId =models.ForeignKey(vino_transferSummary, db_column="summaryId")
    tasteType = models.CharField(null=True, db_column='tasteType', max_length= 100)

    def __unicode__(self):
        return self.tasteType

class vino_transferSummary_Year(models.Model):
    class Meta:
        db_table= "vino_transferSummary_Year"
    summaryId =models.ForeignKey(vino_transferSummary, db_column="summaryId")
    year = models.IntegerField(null=True, db_column='years')

class vino_transferSummary_Mlvolume(models.Model):
    class Meta:
        db_table= "vino_transferSummary_Mlvolume"
    summaryId =models.ForeignKey(vino_transferSummary, db_column="summaryId")
    mlVolume = models.CharField(null=True, db_column='mlVolume', max_length= 100)

class vino_transferSummary_ShopId(models.Model):
    class Meta:
        db_table= "vino_transferSummary_ShopId"
    summaryId =models.ForeignKey(vino_transferSummary, db_column="summaryId")
    shop = models.CharField(null=True, db_column='shop_id', max_length= 100)



#class vino_transferConnect(models.Model):
#    class Meta:
#        db_table="vino_transferConnect"
#    summaryId =models.ForeignKey(vino_transferSummary, db_column="summaryId")
#    itemCode = models.CharField(null=True, db_column='itemCode', index=True, max_length= 255)

class Item(models.Model):
    #productCode = models.CharField(max_length=200)
    productName = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    storeCode = models.CharField(max_length=200)
    idProductNameCluster = models.CharField(max_length=200)
    idProductNameKanaCluster = models.CharField(max_length=200)
    idProductNameNonspaceCluster = models.CharField(max_length=200)
    nameShopChain = models.CharField(max_length=200)

    def __unicode__(self):
        return self.productName


class vino_transferDetail(models.Model):
    class Meta:
        db_table= "vino_transferDetail"
    itemCode = models.CharField(primary_key=True, db_column='itemCode', db_index=True, max_length= 255)
    itemName = models.CharField(null=True, db_column='itemName', max_length= 255)
    itemPrice = models.IntegerField(null=True, db_column='itemPrice')
    marketSite = models.CharField(null=True, db_column='marketSite', max_length= 255)
    shopName = models.CharField(null=True, db_column='shopName', max_length= 255)
    shopCode = models.CharField(null=True, db_column='shopCode', max_length= 255)
    itemAvailability = models.IntegerField(null=True, db_column='itemAvailability') #ダメになったら消すんじゃなくてフラグをOFF（価格履歴を後で追える？）
    itemUrl = models.CharField(null=True, db_column='itemUrl', max_length= 255)
    imageUrl = models.CharField(null=True, db_column='imageUrl', max_length=600)
    summaryId = models.ManyToManyField(vino_transferSummary)