from django.urls import path
from . import views

urlpatterns = [
    path("facebook/post/<str:pk_id>/album", views.selectPostAlbum, name="selectAlbum"),
    path("facebook/post/", views.createPost, name="facebookPost"),
]
