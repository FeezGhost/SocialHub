from django.urls import path
from . import views

urlpatterns = [
    path("default/", views.gallery, name="gallery"),
    path("detail/<str:pk_id>/update/", views.postDetailUpdate, name="updateContentDetails"),
    path("detail/<str:pk_id>/", views.contentDetails, name="contentDetails"),
    path("albums/delete/<str:pk_id>/", views.deleteAlbum, name="deleteAlbum"),
    path("albums/all/", views.albumList, name="albums"),
    path("albums/new/", views.createAlbum, name="createAlbum"),
]
