from datetime import datetime
from platform import platform
from django.db import models
from accounts.models import Client

# Create your models here.

class PlatformChoice(models.TextChoices):
    FACEBOOK = 'Facebook', 'Facebook'
    INSTAGRAM = 'Instagram', 'Instagram'
    LINKEDIN = 'LinkedIn', 'LinkedIn'
    TWITTER = 'Twitter', 'Twitter'

class UserPost(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete= models.SET_NULL)
    platform = models.CharField(choices=PlatformChoice.choices, default=PlatformChoice.FACEBOOK, max_length=128)
    title = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    timeCreated = models.TimeField(auto_now_add=True)
    dateCreated = models.DateField(auto_now_add=True)
    dateToBuy = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.title)

class Tag(models.Model):
    user_post = models.ForeignKey(UserPost, null=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.user_post)+"#"+str(self.name)
