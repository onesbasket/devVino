import datetime
from django.utils import timezone
from django.db import models

class vino_transferSummary(models.Model):
    kanaName =  models.CharField(null=True, db_column='kanaName', max_length = 12000)
    itemPrice = models.FloatField(null=True, db_column='itemPrice')
    itemPriceDeviation = models.FloatField(null=True, db_column='itemPriceDeviation')
    itemPriceCoefficientVariation = models.FloatField(null=True, db_column='itemPriceCoefficientVariation')
    years = models.CharField(null=True, db_column='years', max_length = 255)
    mlVolume = models.CharField(null=True, db_column='mlVolume', max_length = 255)
    reviewAvarage = models.FloatField(null=True, db_column='reviewAvarage')
    reviewCount = models.IntegerField(null=True, db_column='reviewCount')
    tasteType = models.CharField(null=True, db_column='tasteType', max_length = 255)
    countryIds = models.CharField(null=True, db_column='countryId', max_length = 1000)
    regionIds = models.CharField(null=True, db_column='regionId', max_length = 1000)
    grapeIds = models.CharField(null=True, db_column='grapeIds', max_length = 1000)
    
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

#    #-------------#
#class vino_transferDetail(BaseModel):
#	itemCode = CharField(null=True, db_column='itemCode', index = True)
#	itemName = CharField(null=True, db_column='itemName')
#	itemPrice = IntegerField(null=True, db_column='itemPrice')
#	marketSite = CharField(null=True, db_column='marketSite')
#	shopName = CharField(null=True, db_column='shopName')
#	shopCode = CharField(null=True, db_column='shopCode')
#	itemAvailability  = IntegerField(null=True, db_column='itemAvailability')
#	itemUrl =  CharField(null=True, db_column='itemUrl')
#	imageUrl =  CharField(null=True, db_column='imageUrl', max_length=600)
#	#imageUrl
#	
#	class Meta:
#		db_table= "vino_transferDetail"
#
#class vino_transferConnect(BaseModel):
#	summaryId =IntegerField(null=True, db_column='summaryId', index = True)
#	itemCode = CharField(null=True, db_column='itemCode', index = True)
#	
#	class Meta:
#		db_table= "vino_transferConnect"
