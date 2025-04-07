from django.urls import path
from . import views



urlpatterns = [
    path('', views.reparatur, name='reparatur'),
    path('repair-price/', views.repair_price, name='repair_price'),
    path('senddevice/', views.send_device, name='send_device'),
    path('submit-repair-request/', views.submit_repair_request, name='submit_repair_request'),
]
