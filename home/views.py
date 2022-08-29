from django.shortcuts import render
from products.models import Product


def index(request):
    """Return index page"""
    product = Product.objects.all()
    new_products = Product.objects.order_by('-date_added')[:4]
    return render(request, 'home/index.html', {'products': product,
                                               'new_products': new_products})
