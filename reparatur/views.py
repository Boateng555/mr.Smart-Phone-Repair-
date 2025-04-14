from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
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

def send_device(request):
    return render(request, 'reparatur/senddevice.html')

def submit_repair_request(request):
    if request.method == 'POST':
        # Log form data (optional)
        logger.info("Form data received: %s", request.POST)

        device_type = request.POST.get('device_type')
        damage_type = request.POST.get('damage_type')
        damage_description = request.POST.get('damage_description')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('payment_method')

        try:
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
                f'Danke {name} für Ihre Reparaturanfrage.\n\n'
                'Unser Team wird sich bald bei Ihnen melden.\n\n'
                'Mit freundlichen Grüßen,\nMr. Smart Repair',
                'info@mrsmart-repair.com',
                [email],
                fail_silently=False,
            )

            logger.info("Repair request created and email sent.")
            return redirect('success_page')  # Replace with your success template

        except Exception as e:
            logger.error(f"Error during repair request submission: {e}")
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
