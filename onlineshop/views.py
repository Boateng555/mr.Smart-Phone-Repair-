from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Category, Product

def onlineshop(request):
    categories = Category.objects.all()
    products_by_category = {}
    
    for category in categories:
        products = Product.objects.filter(category=category)
        products_by_category[category.name] = products
    
    return render(request, 'onlineshop/onlineshop.html', {'products_by_category': products_by_category})


def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onlineshop')  # Redirect to the shop after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'konto.html')  # Render the login/registration page

def logout_user(request):
    logout(request)
    return redirect('onlineshop')  # Redirect to the shop after logout

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('onlineshop')  # Redirect to the shop after registration
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = UserCreationForm()
    return render(request, 'onlineshop/konto.html', {'form': form})

# onlineshop/views.py
def konto(request):
    return render(request, 'konto.html')  # Render the konto.html template

def konto(request):
    return render(request, 'onlineshop/konto.html')  # Correct template path


# views.py
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'onlineshop/product_detail.html', {'product': product})