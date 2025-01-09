from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('privacy/', views.privacy,name="privacy"),
    path('contactus/', views.contactus,name="contactus"),

]