from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_filters
from django.contrib.gis.db import models
from .models import Inscription, Place
from django  import forms
import datetime
now = datetime.datetime.now()
current_year = now.year
choices = [(u'', u'')]
choices.extend([(year, str(year)) for year in range(current_year - 18, current_year - 5)])
MY_CHOICES2 = (
	('', ''),
    ('CASA', 'CASA'),
    ('TERRENO', 'TERRENO'),
    ('CASA + TERRENO', 'CASA + TERRENO'),
)
MY_CHOICES3 = (
	('', ''),
    ('SI', 'SI'),
    ('NO', 'NO '),
)
class InscriptionFilter(django_filters.FilterSet):
    fn_child = django_filters.CharFilter(lookup_expr='icontains')
    sn_child = django_filters.CharFilter(lookup_expr='icontains')
    year_child = django_filters.NumberFilter(name='dob_child', lookup_expr='year', widget=forms.Select(choices=choices))
    class Meta:
        model = Inscription
        fields = ['fn_child', 'sn_child',]
class PlaceFilter(django_filters.FilterSet):
    typ = django_filters.CharFilter(lookup_expr='icontains', widget=forms.Select(choices=MY_CHOICES2))
    heat = django_filters.CharFilter(widget=forms.Select(choices=MY_CHOICES3))
    capacity = django_filters.NumberFilter(lookup_expr='gt')
    class Meta:
        model = Place
        fields = ['typ', 'heat', 'capacity', 'cost', 'last_group', 'contacts', 'description',]