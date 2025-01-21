from django.urls import path
from . import views




urlpatterns = [
    path('', views.info, name='info'),
    path('home', views.info, name='info'),
    path('repair-price/', views.repair_price, name="repair_price"),  # Add this line
    path('reparatur/repair-price.html', views.repair_price, name="repair_price_alias")
]

