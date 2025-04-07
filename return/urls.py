from django.urls import path

from . import views

urlpatterns = [
    path('', views.return_home, name='return_home'),
]