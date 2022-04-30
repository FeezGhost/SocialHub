from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class GenderChoices(models.TextChoices):
#     MALE = 'Male', 'Male'
#     FEMALE = 'Female', 'Female'
#     OTHER = 'Other', 'Other'


class CreatUserForm(UserCreationForm):
    age =  forms.IntegerField(required=True, help_text='Age must be in numbers and valid', label='Age')
    # gender = forms.ChoiceField(choices=GenderChoices.choices, initial=GenderChoices.OTHER, widget=forms.RadioSelect, required=True, help_text='Please Select your gender.', label='Gender')
    class Meta:
        model =  User
        fields =  ['username', 'first_name', 'last_name', 'email', 'age', 'password1', 'password2']

