
from django.urls import path
from . import views

# localhost:8000/chai
urlpatterns = [
    path('', views.all_chai, name='All_chai'),
    # path('', views.all_chai, name='order'),
]