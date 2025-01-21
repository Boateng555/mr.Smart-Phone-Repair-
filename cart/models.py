from django.db import models
from django.contrib.auth.models import User
from onlineshop.models import Product

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="payment_shipping_addresses")
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return f"Shipping Address - {str(self.id)}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="payments")
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True, blank=True)
    card_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=7)  # Format: MM/YYYY
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment - {str(self.id)}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True, blank=True)  # Link to the shipping address
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the order was last updated
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the order

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    

# models.py
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'