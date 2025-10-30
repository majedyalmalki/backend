# import Home view from the views file
from .views import Home, PlantIndex, PlantDetail, PhotoDetail, ReminderList, ReminderDetail
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plants/', PlantIndex.as_view(), name='plant-index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant-detail'),
    path('plants/<int:plant_id>/add-photo/', PhotoDetail.as_view(), name="create-photo"),
    path('plants/<int:plant_id>/reminders/', ReminderList.as_view(), name='reminder-list'),
    path('plants/<int:plant_id>/reminders/<int:reminder_id>/', ReminderDetail.as_view(), name='reminder-detail'),
]