from django import forms
from django.forms import extras
from django.db import models
from .models import Post, Inscription, Place
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from mapwidgets.widgets import GooglePointFieldWidget
from PIL import Image
from django.core.files import File
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.modelfields import PhoneNumberField



"""
POST Form

"""

class PostForm(forms.ModelForm):


    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    width = forms.FloatField(required=False, widget=forms.HiddenInput())
    height = forms.FloatField(required=False, widget=forms.HiddenInput())
    remove_photo = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text', 'img', 'remove_photo', 'x', 'y', 'width', 'height', )
        widgets = {
            'img': forms.FileInput,
        }
    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        if self.cleaned_data.get('remove_photo'):
            instance.img.delete(False) 
        if commit:
            instance.save()
        return instance
    def save_img(self):
        ist = super(PostForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(ist.img)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((1700, 760), Image.ANTIALIAS)
        resized_image.save(ist.img.path)
        #cropped_image.save(ist.img.path)

        return ist


"""
SIGUP Form

"""



class SignUpForm(UserCreationForm):
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
    now = datetime.datetime.now()
    current_year = now.year
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    gruppo = forms.ChoiceField(choices=MY_CHOICES)
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=range(current_year - 90, current_year - 7)))
    class Meta:
        model = User
        fields = ('username', 'gruppo', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )


"""
INSCRIPTION Form

"""



class InscrForm(forms.ModelForm):
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
    now = datetime.datetime.now()
    current_year = now.year
    first_choice = forms.ChoiceField(choices=MY_CHOICES)
    second_choice = forms.ChoiceField(choices=MY_CHOICES)
    dob_child = forms.DateField(widget=extras.SelectDateWidget(attrs = {
                'display': 'inline-block',}, years=range(current_year - 18, current_year - 5)))
    class Meta:
        model = Inscription
        fields = ('fn_parent', 'sn_parent', 'fn_child', 'sn_child', 'dob_child', 'phone_parent', 'bio_child', 'first_choice', 'second_choice',)



"""
PLACES Form

"""




class PlaceForm(forms.ModelForm):
    MY_CHOICES2 = (
        ('CASA', 'CASA'),
        ('TERRENO', 'TERRENO'),
        ('CASA + TERRENO', 'CASA + TERRENO'),
    )
    MY_CHOICES3 = (
        ('SI', 'SI'),
        ('NO', 'NO '),
    )
    typ = forms.ChoiceField(choices=MY_CHOICES2)
    heat = forms.ChoiceField(choices=MY_CHOICES3)
    class Meta:
        model = Place
        fields = ('typ', 'where', 'coordinates', 'heat', 'capacity', 'cost', 'last_group', 'contacts', 'description',)
        widgets = {
            'coordinates': GooglePointFieldWidget,
        }