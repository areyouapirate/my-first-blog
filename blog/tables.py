import django_tables2 as tables
from .models import Inscription

class InscriptionTable(tables.Table):
    class Meta:
        model = Inscription
        template = 'django_tables2/bootstrap.html'

class PlaceTable(tables.Table):
    class Meta:
        model = Place
        template = 'django_tables2/bootstrap.html'