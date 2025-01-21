from django import template
from onlineshop.models import Product

register = template.Library()

@register.filter
def get_product(product_id):
    return Product.objects.get(id=product_id)