from django.shortcuts import render
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