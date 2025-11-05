# import Home view from the views file
from .views import Home, PlantIndex, PlantDetail, PhotoDetail, ReminderList, ReminderDetail, CreateUserView, LoginView, VerifyUserView, LocationDetail, LocationIndex, AddLocationToPlant, RemoveLocationToPlant
from django.urls import path

urlpatterns = [
# ================================================================================================================= #
#                                                   HOME                                                            #
    path('', Home.as_view(), name='home'),
# ================================================================================================================= #
# ================================================================================================================= #
#                                             Register & Login                                                      #
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
# ================================================================================================================= #
# ================================================================================================================= #
#                                            Plant details & Actions                                                #
    path('plants/', PlantIndex.as_view(), name='plant-index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant-detail'),
    path('plants/<int:plant_id>/add-photo/', PhotoDetail.as_view(), name="create-photo"),
    path('plants/<int:plant_id>/reminders/', ReminderList.as_view(), name='reminder-list'),
    path('plants/<int:plant_id>/reminders/<int:reminder_id>/', ReminderDetail.as_view(), name='reminder-detail'),
# ================================================================================================================= #
# ================================================================================================================= #
#                                              Location Details                                                     #
    path('locations/', LocationIndex.as_view(), name='location-index'),
    path('locations/<int:location_id>/', LocationDetail.as_view(), name='location-detail'),
# ================================================================================================================= #
# ================================================================================================================= #
#                                          Add & Remove location to plant                                           #
    path('plants/<int:plant_id>/associate-location/<int:location_id>/', AddLocationToPlant.as_view(), name='associate-location'),
    path('plants/<int:plant_id>/remove-location/<int:location_id>/', RemoveLocationToPlant.as_view(), name='remove-location'),
# ================================================================================================================= #
]