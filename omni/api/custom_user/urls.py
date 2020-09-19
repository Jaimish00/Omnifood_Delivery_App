from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
# Empty string, because the previous domains are already handelled by api.urls and api.food.urls
router.register('customer', views.CustomerViewSet)
router.register('hotel', views.HotelAdminViewSet)
router.register('delivery', views.DeliveryPersonViewSet)

# TODO: Check if we can merge all the sign out or not

urlpatterns = [
    path('customer/login/', views.customer_signin, name='customer_signin'),
    path('customer/logout/<int:id>/', views.customer_signout, name='customer_signout'),
    path('hotel/login/', views.hotel_signin, name='hotel_signin'),
    path('hotel/logout/<int:id>/', views.hotel_signout, name='hotel_signout'),
    path('delivery/login/', views.delivery_signin, name='delivery_signin'),
    path('delivery/logout/<int:id>/', views.delivery_signout, name='delivery_signout'),
    path('', include(router.urls))
]
