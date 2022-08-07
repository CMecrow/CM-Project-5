from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category

# Create your views here.


def all_products(request):
    """Show all products"""

    full_products = Product.objects.all()
    pagination = Paginator(full_products, 9)
    page_num = request.GET.get('page')
    products = pagination.get_page(page_num)
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            filtered_products = full_products.filter(category__name=categories).order_by('-date_added')
            categories = Category.objects.filter(name__in=categories)
            pagination = Paginator(filtered_products, 9)
            page_num = request.GET.get('page')
            products = pagination.get_page(page_num)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = full_products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
