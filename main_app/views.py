from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlantSerializer, PhotoSerializer, ReminderSerializer
from .models import Plant, Photo, Reminder
from django.shortcuts import get_object_or_404

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the plants api home route!'}
        return Response(content)


class PlantIndex(APIView):
    serializer_class = PlantSerializer
    
    def get(self, request):
        queryset = Plant.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetail(APIView):
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
    def get(self, request, plant_id, reminder_id):
        reminder = get_object_or_404(Reminder, id=reminder_id, plant_id=plant_id)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)


    def delete(self, request, plant_id, reminder_id):
        reminder = get_object_or_404(Reminder, id=reminder_id, plant_id=plant_id)
        reminder.delete()
        return Response({"status":"success"},status=status.HTTP_200_OK)