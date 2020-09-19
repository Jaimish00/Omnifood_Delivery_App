from django.urls import path, include
from . import views

urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.generate_token, name='token.generate'),
    path('processpayment/<str:id>/<str:token>/', views.process_payment, name='payemnt.process'),
]