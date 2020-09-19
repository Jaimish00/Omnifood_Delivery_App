from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
# Empty string, because the previous domains are already handelled by api.urls and api.food.urls
router.register('', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/<str:id>/<str:token>/', views.add, name='order.add'),
]
