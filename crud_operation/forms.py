from dataclasses import field
from tkinter import Widget
from urllib import request
from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Contact
from django.forms.widgets import DateInput

#For user authentication and registration
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User

#Create your form class
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'published_on': DateInput(attrs={'type': 'date'})
        }
        
#User Registration
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


#Creates Contact Us form
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'