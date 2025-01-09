from django.contrib import admin
from django.urls import path,include
from .import views
#listings/23
urlpatterns = [
    path('', views.index,name="listings"),
    path('<int:listing_id>', views.listing,name="listing"),
    path('search', views.search, name="search"),

]