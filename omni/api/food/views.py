from rest_framework import viewsets

from .serializers import FoodSerializer
from .models import Food

# Create your views here.

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('name') # First get all the objects of Model
    serializer_class = FoodSerializer # Class responsible for serialzing the data
    

