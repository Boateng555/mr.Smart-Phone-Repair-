from django.db import models

# Create your models here.
from django.db import models

class RepairRequest(models.Model):
    DEVICE_TYPES = [
        ('Handy', 'Handy'),
        ('Tablet', 'Tablet'),
        ('Laptop', 'Laptop'),
    ]

    DAMAGE_TYPES = [
        ('Display-Schaden', 'Display-Schaden'),
        ('Batterieproblem', 'Batterieproblem'),
        ('Wasserschaden', 'Wasserschaden'),
        ('Rückseite', 'Rückseite'),
        ('Kameraglas', 'Kameraglas'),
        ('Hörmuschel', 'Hörmuschel'),
        ('Ladebuchse', 'Ladebuchse'),
        ('Front Kamera', 'Front Kamera'),
        ('Power Button', 'Power Button'),
        ('Andere', 'Andere'),
    ]

    PAYMENT_METHODS = [
        ('Kreditkarte', 'Kreditkarte'),
        ('PayPal', 'PayPal'),
        ('Überweisung', 'Überweisung'),
    ]

    device_type = models.CharField(max_length=50, choices=DEVICE_TYPES)
    damage_type = models.CharField(max_length=50, choices=DAMAGE_TYPES)
    damage_description = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repair Request by {self.name} for {self.device_type}"