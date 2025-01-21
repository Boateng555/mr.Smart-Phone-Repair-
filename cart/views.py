from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from onlineshop.models import Product  # Import Product from the correct app
from .models import Payment, ShippingAddress, Order, Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def cart(request):
    cart = request.session.get('cart', {})
    print("Cart session data:", cart)  # Debugging: Print the cart session data
    subtotal = 0
    valid_cart = {}  # To store valid product IDs and quantities

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            subtotal += product.price * quantity
            valid_cart[product_id] = quantity  # Add valid product to the cart
        except Product.DoesNotExist:
            print(f"Product with ID {product_id} does not exist.")  # Debugging: Print missing product IDs
            continue  # Skip this product and continue with the next one

    # Update the session with only valid products
    request.session['cart'] = valid_cart

    delivery_fee = 5  # Fixed delivery fee
    total = subtotal + delivery_fee

    context = {
        'cart': valid_cart,  # Use the cleaned cart data
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'total': total,
    }
    return render(request, "cart/cart.html", context)

def cart_add(request, product_id):
    """
    Add a product to the cart.
    """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect('onlineshop')  # Redirect to the shop page if the product doesn't exist

    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def cart_delete(request, product_id):
    """
    Remove a product from the cart.
    """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect('cart')

    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

def cart_update(request, product_id):
    """
    Update the quantity of a product in the cart.
    """
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            messages.error(request, "Invalid quantity.")
            return redirect('cart')

        if quantity <= 0:
            messages.error(request, "Quantity must be greater than 0.")
            return redirect('cart')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            messages.error(request, "Product not found.")
            return redirect('cart')

        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            del cart[str(product_id)]
        request.session['cart'] = cart

    return redirect('cart')

def checkout(request):
    """
    Display the checkout page with the cart items and total.
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    subtotal = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal += product.price * quantity
    delivery_fee = 5  # Fixed delivery fee
    total = subtotal + delivery_fee

    context = {
        'cart_items': cart.items(),
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'total': total,
    }
    return render(request, "cart/checkout.html", context)

@login_required
def payment(request):
    """
    Handle the payment process.
    """
    if request.method == 'POST':
        # Get payment details from the form
        card_name = request.POST.get('card-name')
        card_number = request.POST.get('card-number')
        expiry_date = request.POST.get('expiry-date')
        cvv = request.POST.get('cvv')
        total = float(request.POST.get('total', 0))

        # Get shipping address details from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')

        # Validate required fields
        if not all([full_name, email, address1, city, country]):
            return render(request, "cart/payment.html", {
                'error': 'Please fill out all required fields.'
            })

        # Get or create the shipping address for the user
        shipping_address, created = ShippingAddress.objects.get_or_create(
            user=request.user,
            defaults={
                'full_name': full_name,
                'email': email,
                'address1': address1,
                'address2': address2,
                'city': city,
                'state': state,
                'zipcode': zipcode,
                'country': country,
            }
        )

        # Create the order
        order = Order.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            total_amount=total
        )

        # Clear the cart after successful payment
        if 'cart' in request.session:
            del request.session['cart']

        return redirect('payment_success')  # Redirect to a success page

    # Calculate total from the cart
    cart = request.session.get('cart', {})
    subtotal = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal += product.price * quantity
    delivery_fee = 5  # Fixed delivery fee
    total = subtotal + delivery_fee

    context = {
        'total': total,
    }
    return render(request, "cart/payment.html", context)

def payment_success(request):
    """
    Display a success message after a payment is completed.
    """
    return render(request, "cart/payment_success.html")

def konto(request):
    """
    Handle user account functionality (login and registration).
    """
    if request.method == 'POST':
        # Check if the form is for login or registration
        if 'login' in request.POST:
            # Handle login
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome back, {username}!")
                    return redirect('cart')  # Redirect to the cart page after login
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")

        elif 'register' in request.POST:
            # Handle registration
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log the user in after registration
                messages.success(request, f"Account created successfully for {user.username}!")
                return redirect('cart')  # Redirect to the cart page after registration
            else:
                messages.error(request, "Error creating account. Please check the form.")

    else:
        # Display empty forms for login and registration
        login_form = AuthenticationForm()
        register_form = UserCreationForm()

    return render(request, "cart/konto.html", {
        'login_form': login_form,
        'register_form': register_form,
    })

def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('cart')  # Redirect to the cart page after logout