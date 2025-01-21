from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RepairRequest

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'damage_type', 'created_at')
    list_filter = ('device_type', 'damage_type', 'created_at')
    search_fields = ('name', 'email', 'phone')