from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    '''
    Adds more fields to user creation form
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile picture
    '''
    neighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all())
    class Meta:
        model = Profile
        fields = ['bio','neighborhood','profile_pic']
        
        
class BuisnessesForm(forms.ModelForm):
    '''
    Form for advertising a a buisness
    '''
    class Meta:
        model = Business
        fields = ["business_name","business_email","business_number"]
        

class StoryForm(forms.ModelForm):
    '''
    Form for uploading stories
    '''
    class Meta:
        model = Stories
        fields = ["category","headline","story"]