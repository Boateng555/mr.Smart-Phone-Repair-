from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add/<int:product_id>/', views.cart_add, name="cart_add"),
    path('delete/<int:product_id>/', views.cart_delete, name="cart_delete"),
    path('update/<int:product_id>/', views.cart_update, name="cart_update"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),
    path('payment/success/', views.payment_success, name="payment_success"),
    path('konto/', views.konto, name="konto"),  # Add the konto URL
    path('logout/', views.logout_view, name="logout"),  # Add the logout URL
]