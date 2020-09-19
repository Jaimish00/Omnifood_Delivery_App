from rest_framework import serializers

from .models import Order
from ..custom_user.serializers import HotelSerializer, DeliveryPersonSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    hotel = HotelSerializer()
    delivery_person = DeliveryPersonSerializer()
    class Meta:
        model = Order
        fields = ('customer', 'hotel', 'delivery_person', 'food_items', 'total_items', 'transaction_id')
