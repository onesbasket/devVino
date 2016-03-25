# coding: utf-8

from django import forms
from listSummary.models import vino_transferSummary,tagCountry, tagRegion, tagGrape,  vino_transferSummary_TasteType


class KakikomiForm(forms.Form):
    lowPrice = forms.IntegerField(label="", required=False, widget=forms.TextInput(attrs={'style': 'width:80px'}))
    highPrice = forms.IntegerField(label="", required=False, widget=forms.TextInput(attrs={'style': 'width:80px'}))
    lowYears = forms.IntegerField(required=False,)
    highYears = forms.IntegerField(required=False,)
    lowVolume = forms.IntegerField(required=False,)
    highVolume = forms.IntegerField(required=False,)
    reviewAvarage = forms.IntegerField(required=False,)


class selectionListForm(forms.Form):
    grapeIds = forms.ModelChoiceField(queryset = tagGrape.objects.none(),
        #label='aaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        #queryset= tagGrape.objects.values_list('name', flat=True),
        #queryset= tagGrape.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        empty_label=None
    )
    regionIds = forms.ModelChoiceField(queryset = tagRegion.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        empty_label=None
    )
    countryIds = forms.ModelChoiceField(queryset = tagCountry.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        empty_label=None
    )
    #def __init__(self, *args, **kwargs):
    #    super(selectionListForm, self).__init__(*args, **kwargs)
    #    self.fields['reqGrape'].queryset = tagGrape.objects.all()