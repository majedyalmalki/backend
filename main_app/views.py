from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import PlantSerializer, PhotoSerializer, ReminderSerializer, UserSerializer, LocationSerializer
from .models import Plant, Photo, Reminder, User, Location
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404



# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class LoginView(APIView):

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data}
                return Response(content, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            try:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh),'access': str(refresh.access_token),'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
            except Exception as token_error:
                return Response({"detail": "Failed to generate token.", "error": str(token_error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            return Response({"detail": "Unexpected error occurred.", "error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the plants api home route!'}
        return Response(content)


class PlantIndex(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlantSerializer
    
    def get(self, request):
        queryset = Plant.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlantSerializer

    def get(self, request, plant_id):
        plant = get_object_or_404(Plant, id=plant_id)
        serializer = self.serializer_class(plant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, plant_id):
        plant = get_object_or_404(Plant, id=plant_id)
        serializer = self.serializer_class(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, plant_id):
        plant = get_object_or_404(Plant, id=plant_id)
        plant.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)



class PhotoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PhotoSerializer

    def post(self, request, plant_id):
        data = request.data.copy()
        data["plant"] = int(plant_id)

        Photo.objects.filter(plant=plant_id).delete()

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(PlantSerializer(get_object_or_404(Plant, id=plant_id)).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ReminderList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, plant_id):
        reminders = Reminder.objects.filter(plant_id=plant_id)
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)

    def post(self, request, plant_id):
        data = request.data.copy()
        data['plant'] = plant_id

        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReminderDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, plant_id, reminder_id):
        reminder = get_object_or_404(Reminder, id=reminder_id, plant_id=plant_id)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)


    def delete(self, request, plant_id, reminder_id):
        reminder = get_object_or_404(Reminder, id=reminder_id, plant_id=plant_id)
        reminder.delete()
        return Response({"status":"success"},status=status.HTTP_200_OK)



class LocationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, plant_id):
        plant = get_object_or_404(Plant, id=plant_id)
        locations = plant.locations.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, plant_id):
        plant = get_object_or_404(Plant, id=plant_id)
        serializer = LocationSerializer(data=request.data)
        
        if serializer.is_valid():
            location = serializer.save()
            plant.locations.add(location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, plant_id, location_id):
        plant = get_object_or_404(Plant, id=plant_id)
        location = get_object_or_404(Location, id=location_id)

        if location in plant.locations.all():
            serializer = LocationSerializer(location, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Location not found in this plant.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, plant_id, location_id):
        plant = get_object_or_404(Plant, id=plant_id)
        location = get_object_or_404(Location, id=location_id)

        if location in plant.locations.all():
            plant.locations.remove(location)
            location.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'error': 'Location not found in this plant.'}, status=status.HTTP_404_NOT_FOUND)
