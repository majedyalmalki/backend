# import Home view from the views file
from .views import Home, PlantIndex, PlantDetail
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plants/', PlantIndex.as_view(), name='plant-index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant-detail'),
]