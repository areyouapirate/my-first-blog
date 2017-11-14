from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_filters
from .models import Inscription
from django  import forms
import datetime
now = datetime.datetime.now()
current_year = now.year
choices = [(u'', u'')]
choices.extend([(year, str(year)) for year in range(current_year - 18, current_year - 5)])

class InscriptionFilter(django_filters.FilterSet):
    fn_child = django_filters.CharFilter(lookup_expr='icontains')
    sn_child = django_filters.CharFilter(lookup_expr='icontains')
    year_child = django_filters.NumberFilter(name='dob_child', lookup_expr='year', widget=forms.Select(choices=choices))
    class Meta:
        model = Inscription
        fields = ['fn_child', 'sn_child',]