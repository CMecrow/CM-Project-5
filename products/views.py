from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
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
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    pagination = Paginator(products, 9)
    page_num = request.GET.get('page')
    products = pagination.get_page(page_num)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Show an individual product"""
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        comments = Comment.objects.order_by('created_on')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.save()
            comment_form = CommentForm()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment successfully submitted!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            comment_form = CommentForm()
    else:
        product = get_object_or_404(Product, pk=product_id)
        comments = Comment.objects.order_by('created_on')
        related_products = Product.objects.filter(category=product.category).exclude(pk=product_id).order_by('?')[:4]
        comment_form = CommentForm()

        context = {
            'product': product,
            'comments': comments,
            'comment_form': comment_form,
            'related_products': related_products,
        }

        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """Admin add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Only site admins can access this page')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product\
                             to the store')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product to the store,\
                           please check form')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'hide_message_bag': True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit an existing product"""
    if not request.user.is_superuser:
        messages.error(request, 'Only site admins can access this page')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to update {product.name},\
                           please check details')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete an existing product"""
    if not request.user.is_superuser:
        messages.error(request, 'Only site admins can access this page')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Successfully deleted {product.name}')
    return redirect(reverse('products'))
