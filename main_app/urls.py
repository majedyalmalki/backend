# import Home view from the views file
from .views import Home, PlantIndex, PlantDetail, PhotoDetail, ReminderList, ReminderDetail, CreateUserView, LoginView, VerifyUserView, LocationView
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('plants/', PlantIndex.as_view(), name='plant-index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant-detail'),
    path('plants/<int:plant_id>/add-photo/', PhotoDetail.as_view(), name="create-photo"),
    path('plants/<int:plant_id>/reminders/', ReminderList.as_view(), name='reminder-list'),
    path('plants/<int:plant_id>/reminders/<int:reminder_id>/', ReminderDetail.as_view(), name='reminder-detail'),
    path('plants/<int:plant_id>/locations/', LocationView.as_view(), name='plant_location'),
    path('plants/<int:plant_id>/locations/<int:location_id>/', LocationView.as_view(), name='plant_location_detail'),
]