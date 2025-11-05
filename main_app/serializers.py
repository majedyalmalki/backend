from rest_framework import serializers
from .models import Plant, Photo, Reminder, Location
from django.contrib.auth.models import User


# ================================================================================================================= #
#                                               Photo Serializer                                                    #
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
# ================================================================================================================= #
# ================================================================================================================= #
#                                               Location Serializer                                                 #
class LocationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Location
        fields = '__all__'
# ================================================================================================================= #


# ================================================================================================================= #
#                                               Plant Serializer                                                    #
class PlantSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True, required=False)
    photo = PhotoSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Plant
        fields = '__all__'
# ================================================================================================================= #
# ================================================================================================================= #
#                                               Reminder Serializer                                                 #
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
# ================================================================================================================= #

# ================================================================================================================= #
#                                                 User Serializer                                                   #
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
        return user
# ================================================================================================================= #
