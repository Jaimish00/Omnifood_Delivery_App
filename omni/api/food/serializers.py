from rest_framework import serializers
from ..custom_user.serializers import HotelSerializer
from .models import Food

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    hotel = HotelSerializer()
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    class Meta:
        model = Food
        fields = ('name', 'description', 'price', 'image', 'hotel')