from django.forms import ModelForm
from .models import PostAlbum



class PostAlbumForm(ModelForm):
    
    class Meta:
        model =  PostAlbum
        fields = ['name']
