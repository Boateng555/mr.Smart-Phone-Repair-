from django.urls import path
from . import views
from .views import home, DatenschutzView, AGBView
from .views import ImpressumView



urlpatterns = [
    path('', views.home, name='info-home'),  # Handles the root URL
    path('datenschutz/', DatenschutzView.as_view(), name='datenschutz'),
    path('agb/', AGBView.as_view(), name='agb'),
    path('impressum/', ImpressumView.as_view(), name='impressum'),
]


