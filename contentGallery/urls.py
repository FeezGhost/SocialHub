from django.urls import path
from . import views

urlpatterns = [
    path("default/", views.gallery, name="gallery")
]
