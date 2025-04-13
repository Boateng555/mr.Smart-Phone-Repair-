from django.contrib import admin

# Register your models here.

from .models import RepairRequest

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'damage_type', 'email', 'phone', 'payment_method', 'created_at')
    search_fields = ('name', 'email', 'device_type', 'damage_type')
    list_filter = ('device_type', 'damage_type', 'payment_method')
