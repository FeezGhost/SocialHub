from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.userLogin, name="login"),
    path('signup/', views.userSignup, name="signup"),
    path('logout/', views.logoutView, name="logout"),
    path('home/', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('profile/update', views.profileUpdate, name="updateProfile"),
]