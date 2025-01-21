from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import RepairRequest

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
        device_type = request.POST.get('device_type')
        damage_type = request.POST.get('damage_type')
        damage_description = request.POST.get('damage_description')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('payment_method')

        RepairRequest.objects.create(
            device_type=device_type,
            damage_type=damage_type,
            damage_description=damage_description,
            name=name,
            email=email,
            phone=phone,
            payment_method=payment_method
        )
        return redirect('send_device')  # Redirect to the senddevice page after submission
    return render(request, 'reparatur/senddevice.html')