from django import forms
from django.forms import extras
from django.db import models
from .models import Post, Inscription, Place
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from mapwidgets.widgets import GooglePointFieldWidget

MY_CHOICES = (
    ('None', 'Nessuno'),
    ('PT1', 'Pistoia 1'),
    ('PT2', 'Pistoia 2'),
    ('PT3', 'Pistoia 3'),
    ('PT4', 'Pistoia 4'),
    ('SG1', 'San Giorgio 1'),
    ('QU1', 'Quarrata 1'),
    ('MC1', 'Massa e Cozzile 1'),
    ('CU1', 'Chiesina Uzzanese 1'),
    ('UZ 1', 'Uzzano 1'), 
)
MY_CHOICES2 = (
    ('CASA', 'CASA'),
    ('TERRENO', 'TERRENO'),
    ('CASA + TERRENO', 'CASA + TERRENO'),
)
MY_CHOICES3 = (
    ('SI', 'SI'),
    ('NO', 'NO '),
)
now = datetime.datetime.now()
current_year = now.year
class PostForm(forms.ModelForm):
    img = forms.FileField(required=False)
    class Meta:
        model = Post
        fields = ('title', 'text', 'img',)
		

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    gruppo = forms.ChoiceField(choices=MY_CHOICES)
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=range(current_year - 90, current_year - 7)))
    class Meta:
        model = User
        fields = ('username', 'gruppo', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )
class InscrForm(forms.ModelForm):
    first_choice = forms.ChoiceField(choices=MY_CHOICES)
    second_choice = forms.ChoiceField(choices=MY_CHOICES)
    dob_child = forms.DateField(widget=extras.SelectDateWidget(years=range(current_year - 18, current_year - 5)))
    class Meta:
        model = Inscription
        fields = ('fn_parent', 'sn_parent', 'fn_child', 'sn_child', 'dob_child', 'bio_child', 'first_choice', 'second_choice',)
class PlaceForm(forms.ModelForm):
    typ = forms.ChoiceField(choices=MY_CHOICES2)
    heat = forms.ChoiceField(choices=MY_CHOICES3)
    class Meta:
        model = Place
        fields = ('typ', 'where', 'coordinates', 'heat', 'capacity', 'cost', 'last_group', 'contacts', 'description',)
        widgets = {
            'coordinates': GooglePointFieldWidget,
        }