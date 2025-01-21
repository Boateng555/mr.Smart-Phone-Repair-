from django.shortcuts import render

def info(request):
    return render(request, "info/index.html")

def repair_price(request):
    repair_prices = [
        {"manufacturer": "Apple", "model": "iPhone 12", "display": "€100", "battery": "€50"},
        {"manufacturer": "Samsung", "model": "Galaxy S21", "display": "€120", "battery": "€60"},
        # Add more data here
    ]
    context = {
        'repair_prices': repair_prices,
    }
    return render(request, "info/repair-price.html", context)