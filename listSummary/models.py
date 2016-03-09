# coding: utf-8
from django.db import models

# Create your models here.
class tagGrape(models.Model):
    class Meta:
        db_table= "tagGrape"
    name = models.CharField(null=True, db_column='name', max_length =100)

class tagCountry(models.Model):
    class Meta:
        db_table= "tagCountry"
    name = models.CharField(null=True, db_column='name', max_length =100)

class tagRegion(models.Model):
    class Meta:
        db_table= "tagRegion"
    name = models.CharField(null=True, db_column='name', max_length =100)


class vino_transferSummary(models.Model):
    class Meta:
        db_table = "vino_transferSummary"

    kanaName =  models.CharField(null=True, db_column='kanaName', max_length = 12000)
    itemPrice = models.FloatField(null=True, db_column='itemPrice')
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