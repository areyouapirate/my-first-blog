from django import forms
from django.forms import extras
from django.db import models
from .models import Post, Inscription
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
MY_CHOICES = (
    ('Pistoia 1', 'Pistoia 1'),
    ('Pistoia 2', 'Pistoia 2'),
    ('Pistoia 3', 'Pistoia 3'),
    ('Pistoia 4', 'Pistoia 4'),
    ('San Giorgio 1', 'San Giorgio 1'),
    ('Quarrata 1', 'Quarrata 1'),
    ('Massa e Cozzile 1', 'Massa e Cozzile 1'),
    ('Chiesina Uzzanese 1', 'Chiesina Uzzanese 1'),
    ('Uzzano 1', 'Uzzano 1'),
)
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
		

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    gruppo = forms.ChoiceField(choices=MY_CHOICES)
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=range(1950, 2017)))
    class Meta:
        model = User
        fields = ('username', 'gruppo', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )
class InscrForm(forms.ModelForm):
    first_choice = forms.ChoiceField(choices=MY_CHOICES)
    second_choice = forms.ChoiceField(choices=MY_CHOICES)
    dob_child = forms.DateField(widget=extras.SelectDateWidget(years=range(1950, 2017)))
    class Meta:
        model = Inscription
        fields = ('fn_parent', 'sn_parent', 'fn_child', 'sn_child', 'dob_child', 'bio_child', 'first_choice', 'second_choice',)