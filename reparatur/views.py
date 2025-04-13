from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import RepairRequest
import logging

logger = logging.getLogger(__name__)


def reparatur(request):
    return render(request, 'reparatur/reparatur.html')


def repair_price(request):
    category = request.GET.get('category', '')
    context = {
        'category': category,
    }
    return render(request, 'reparatur/repair-price.html', context)

# Your send_device view
def send_device(request):
    return render(request, 'reparatur/senddevice.html')







@csrf_exempt  # remove this if you have CSRF tokens properly setup
def submit_repair_request(request):
    if request.method == 'POST':
        try:
            device_type = request.POST.get('device_type')
            damage_type = request.POST.get('damage_type')
            damage_description = request.POST.get('damage_description')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            payment_method = request.POST.get('payment_method')

            # Save to DB
            repair_request = RepairRequest.objects.create(
                device_type=device_type,
                damage_type=damage_type,
                damage_description=damage_description,
                name=name,
                email=email,
                phone=phone,
                payment_method=payment_method
            )

            # Send email to customer
            send_mail(
                'Reparaturanfrage erhalten – Mr. Smart Repair',
                'Danke für Ihre Anfrage. Wir melden uns bald bei Ihnen!',
                'kwameb792@gmail.com',  # Make sure this matches your email settings
                [email],
                fail_silently=False,
            )

            return JsonResponse({'success': True, 'message': 'Repair request submitted and email sent.'})
        except Exception as e:
            logger.error("Error during repair request submission: %s", e)
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})
