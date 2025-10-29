# import Home view from the views file
from .views import Home, PlantIndex
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plants/', PlantIndex.as_view(), name='plant-index'),
    
]