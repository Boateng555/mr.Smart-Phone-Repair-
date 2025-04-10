from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product, Profile
import datetime

from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        items = OrderItem.objects.filter(order=pk)

        if request.POST:
            status = request.POST['shipping_status']
            now = datetime.datetime.now()
            Order.objects.filter(id=pk).update(
                shipped=status == "true",
                date_shipped=now if status == "true" else None
            )
            messages.success(request, "Shipping Status Updated")
            return redirect('home')

        return render(request, 'payment/orders.html', {"order": order, "items": items})
    messages.success(request, "Access Denied")
    return redirect('home')

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)
        if request.POST:
            order_id = request.POST['num']
            Order.objects.filter(id=order_id).update(shipped=True, date_shipped=datetime.datetime.now())
            messages.success(request, "Shipping Status Updated")
            return redirect('home')

        return render(request, "payment/not_shipped_dash.html", {"orders": orders})
    messages.success(request, "Access Denied")
    return redirect('home')

def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        if request.POST:
            order_id = request.POST['num']
            Order.objects.filter(id=order_id).update(shipped=False)
            messages.success(request, "Shipping Status Updated")
            return redirect('home')

        return render(request, "payment/shipped_dash.html", {"orders": orders})
    messages.success(request, "Access Denied")
    return redirect('home')

def process_order(request):
    if not request.POST:
        messages.success(request, "Access Denied")
        return redirect('home')

    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total() * 0.93  # Convert to EUR

    my_shipping = request.session.get('my_shipping')
    if not my_shipping:
        messages.error(request, "Shipping info not found.")
        return redirect('checkout')

    full_name = my_shipping['shipping_full_name']
    email = my_shipping['shipping_email']
    shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
    amount_paid = totals

    user = request.user if request.user.is_authenticated else None
    create_order = Order(user=user, full_name=full_name, email=email,
                         shipping_address=shipping_address, amount_paid=amount_paid)
    create_order.save()

    for product in cart_products:
        price = (product.sale_price if product.is_sale else product.price) * 0.93
        quantity = quantities.get(str(product.id), 0)
        OrderItem.objects.create(order=create_order, product=product, user=user, quantity=quantity, price=price)

    if user:
        Profile.objects.update_or_create(user=user, defaults={"old_cart": ""})

    cart.clear()
    messages.success(request, "Order Placed!")
    return redirect('home')

def billing_info(request):
    if not request.POST:
        messages.success(request, "Access Denied")
        return redirect('home')

    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()

    request.session['my_shipping'] = request.POST.dict()
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': totals,
        'item_name': 'Product Order',
        'no_shipping': '2',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'EUR',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("payment_success")}',
        'cancel_return': f'http://{host}{reverse("payment_failed")}',
    }

    paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    billing_form = PaymentForm()
    return render(request, "payment/billing_info.html", {
        "paypal_form": paypal_form,
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals,
        "shipping_info": request.POST,
        "billing_form": billing_form
    })

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    else:
        shipping_form = ShippingForm(request.POST or None)

    return render(request, "payment/checkout.html", {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals,
        "shipping_form": shipping_form,
    })

def payment_success(request):
    return render(request, "payment/payment_success.html")

def payment_failed(request):
    return render(request, "payment/payment_failed.html")
