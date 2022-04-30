from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.userLogin, name="login"),
    path('singup/', views.userSignup, name="signup"),
]