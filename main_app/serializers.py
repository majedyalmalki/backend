from rest_framework import serializers
from .models import Plant, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)
    class Meta:
        model = Plant
        fields = '__all__'