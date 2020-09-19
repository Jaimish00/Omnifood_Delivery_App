from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('food/', include('api.food.urls')),
    path('user/', include('api.custom_user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
