from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlantSerializer
from .models import Plant

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the plants api home route!'}
        return Response(content)


class PlantIndex(APIView):
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