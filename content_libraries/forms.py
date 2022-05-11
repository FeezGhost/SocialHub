from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'


# class GenderChoices(models.TextChoices):
#     MALE = 'Male', 'Male'
#     FEMALE = 'Female', 'Female'
#     OTHER = 'Other', 'Other'


    # age =  forms.IntegerField(required=True, help_text='Age must be in numbers and valid', label='Age')
    # gender = forms.ChoiceField(choices=GenderChoices.choices, initial=GenderChoices.OTHER, widget=forms.RadioSelect, required=True, help_text='Please Select your gender.', label='Gender')




    # client = models.ForeignKey(Client, null=True, on_delete= models.SET_NULL)
    # platform = models.CharField(choices=PlatformChoice.choices, default=PlatformChoice.FACEBOOK, max_length=128)
    # title = models.CharField(max_length=200, null=True, blank=True)
    # picture = models.ImageField(null=True, blank=True)
    # description = models.TextField(blank=True, null=True)
    # location = models.CharField(max_length=500, blank=True, null=True)
    # lat = models.FloatField(default=0)
    # lng = models.FloatField(default=0)
    # timeCreated = models.TimeField(auto_now_add=True)
    # dateCreated = models.DateField(auto_now_add=True)
    # dateToBuy = models.DateTimeField(default=datetime.now)
class UserPostForm(ModelForm):
    
    class Meta:
        model =  UserPost
        fields = '__all__'
        exclude = ['client', 'lat', 'lng', 'timeCreated', 'dateCreated', 'dateToBuy', 'picture','platform' ]
