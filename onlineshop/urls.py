# onlineshop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.onlineshop, name='onlineshop'),  # Main shop page
    path('about/', views.about, name='about'),  # About page
    path('login/', views.login_user, name='login'),  # Login page
    path('logout/', views.logout_user, name='logout'),  # Logout page
    path('register/', views.register_user, name='register'),  # Registration page
]