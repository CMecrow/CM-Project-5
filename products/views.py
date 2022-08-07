from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

# Create your views here.


def all_products(request):
    """Show all products"""

    pagination = Paginator(Product.objects.all(), 9)
    page_num = request.GET.get('page')
    products = pagination.get_page(page_num)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Show an individual product"""

    product = get_object_or_404(Product, pk=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product_id).order_by('?')[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_detail.html', context)
