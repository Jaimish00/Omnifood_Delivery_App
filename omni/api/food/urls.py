from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
# Empty string, because the previous domains are already handelled by api.urls and api.food.urls
router.register('', views.FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
