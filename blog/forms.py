from django import forms
from django.db import models
from .models import Post
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
    class Meta:
        model = User
        fields = ('username', 'gruppo', 'email', 'password1', 'password2', )