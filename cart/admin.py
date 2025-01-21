from django.contrib import admin
from .models import ShippingAddress  # Import the ShippingAddress model
from .models import Order, ShippingAddress  



# Register the ShippingAddress model
@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'city', 'country')  # Customize the fields displayed in the admin list view
    search_fields = ('user__username', 'full_name', 'email', 'city', 'country')  # Add search functionality
    list_filter = ('city', 'country')  # Add filters for city and country


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shipping_address', 'total_amount', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'shipping_address__full_name')