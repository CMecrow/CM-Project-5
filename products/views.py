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
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = full_products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            sorted_products = full_products.order_by(sortkey)
            pagination = Paginator(sorted_products, 9)
            page_num = request.GET.get('page')
            products = pagination.get_page(page_num)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            filtered_products = full_products.filter(category__name__in=categories).order_by('-date_added')
            categories = Category.objects.filter(name__in=categories)
            pagination = Paginator(filtered_products, 9)
            page_num = request.GET.get('page')
            products = pagination.get_page(page_num)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            filtered_products = full_products.filter(queries)
            pagination = Paginator(filtered_products, 9)
            page_num = request.GET.get('page')
            products = pagination.get_page(page_num)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
