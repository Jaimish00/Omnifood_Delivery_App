from django.db import models
from ..custom_user.models import HotelAdmin
import datetime


TIME_CHOICES = (
    ('00:00:00', 'Midnight'),
    ('01:00:00', '01 AM'),
    ('02:00:00', '02 AM'),
    ('03:00:00', '03 AM'),
    ('04:00:00', '04 AM'),
    ('05:00:00', '05 AM'),
    ('06:00:00', '06 AM'),
    ('07:00:00', '07 AM'),
    ('08:00:00', '08 AM'),
    ('09:00:00', '09 AM'),
    ('10:00:00', '10 AM'),
    ('11:00:00', '11 AM'),
    ('12:00:00', 'Noon'),
    ('13:00:00', '01 PM'),
    ('14:00:00', '02 PM'),
    ('15:00:00', '03 PM'),
    ('16:00:00', '04 PM'),
    ('17:00:00', '05 PM'),
    ('18:00:00', '06 PM'),
    ('19:00:00', '07 PM'),
    ('20:00:00', '08 PM'),
    ('21:00:00', '09 PM'),
    ('22:00:00', '10 PM'),
    ('23:00:00', '11 PM'), 
)


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.FloatField(max_length=20, default=0)
    is_available = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    hotel = models.ForeignKey(HotelAdmin, on_delete=models.CASCADE, related_name='food', default=True, null=True)
    state_speciality = models.CharField(max_length=30, default=True, null=True)
    schedule_start = models.CharField(max_length=10, choices=TIME_CHOICES, default='00:00:00')
    schedule_end = models.CharField(max_length=10, choices=TIME_CHOICES, default='23:00:00')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # Instead of Generic Name, write the Food name when need to be displayed
        return self.name


    