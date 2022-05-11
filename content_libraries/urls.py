from django.urls import path
from . import views

urlpatterns = [
    path("facebook/post/", views.createPost, name="facebookPost")
]
