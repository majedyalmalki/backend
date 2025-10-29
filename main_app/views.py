from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlantSerializer
from .models import Plant
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