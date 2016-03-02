#from Consolidate.models import Item
from django.contrib import admin



class ConsolidateAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['productName']}),
    ]
    list_display = ('productCode', 'productName',)
    search_fields = ['productName']
    
#admin.site.register(Consolidate, ConsolidateAdmin)
