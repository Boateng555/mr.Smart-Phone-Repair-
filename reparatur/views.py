from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import RepairRequest
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def reparatur(request):
     return render(request, 'reparatur/reparatur.html')


def repair_price(request):
    category = request.GET.get('category', '')
    context = {
        'category': category,
    }
    return render(request, 'reparatur/repair-price.html', context)


def send_device(request):
    return render(request, 'reparatur/senddevice.html')

logger = logging.getLogger(__name__)

@csrf_exempt  # Temporarily disable CSRF for testing
def submit_repair_request(request):
    if request.method == 'POST':
        logger.info("Form data received: %s", request.POST)

        device_type = request.POST.get('device_type')
        damage_type = request.POST.get('damage_type')
        damage_description = request.POST.get('damage_description')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('payment_method')

        # Save the repair request to the database
        try:
            repair_request = RepairRequest.objects.create(
                device_type=device_type,
                damage_type=damage_type,
                damage_description=damage_description,
                name=name,
                email=email,
                phone=phone,
                payment_method=payment_method
            )
            logger.info("Repair request created: %s", repair_request)
            return JsonResponse({'success': True, 'message': 'Repair request created successfully.'})
        except Exception as e:
            logger.error("Failed to create repair request: %s", e)
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})