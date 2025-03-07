from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='About'),
    path('menu/', views.menu, name='menu'),
    path('locations/', views.locations, name='Locations'),
    path('review/', views.review, name='review'),
]