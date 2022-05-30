from django.db import models
from accounts.models import Client

from content_libraries.models import UserPost

# Create your models here.

class PostAlbum(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete= models.SET_NULL, related_name='client_albums')
    posts = models.ManyToManyField(UserPost)
    name = models.CharField(max_length=128, blank=False)
    def __str__(self):
        return str(self.name)
