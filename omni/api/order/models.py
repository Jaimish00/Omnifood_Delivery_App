from django.db import models
from ..custom_user.models import Customer, HotelAdmin, User, DeliveryPerson
from ..food.models import Food
# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(HotelAdmin, on_delete=models.CASCADE, null=True, blank=True, related_name='order')
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, null=True, blank=True, related_name='order')

    food_items = models.CharField(max_length=500)
    total_items = models.CharField(max_length=50, default=0)
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
