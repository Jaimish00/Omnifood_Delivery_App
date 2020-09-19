from django.contrib import admin
from .models import Customer, HotelAdmin, DeliveryPerson, User

admin.site.register(Customer)
admin.site.register(HotelAdmin)
admin.site.register(DeliveryPerson)
admin.site.register(User)