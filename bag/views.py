from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """A view to return the shopping bag"""

    context = {
        'hide_message_bag': True
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """Add a quantity of the selected product to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    skate_size = None

    if 'skate_size' in request.POST:
        skate_size = request.POST['skate_size']

    clothes_size = None

    if 'clothes_size' in request.POST:
        clothes_size = request.POST['clothes_size']

    bag = request.session.get('bag', {})

    if skate_size:
        if item_id in list(bag.keys()):
            if skate_size in list(bag[item_id]['skates_by_size'].keys()):
                bag[item_id]['skates_by_size'][skate_size] += quantity
                messages.success(request, f'Updated {product.name} size\
                                 {skate_size.upper()} quantity to\
                                 {bag[item_id]["skates_by_size"][skate_size]}')
            else:
                bag[item_id]['skates_by_size'][skate_size] = quantity
                messages.success(request, f'Added {product.name} size\
                                 {skate_size.upper()} to your bag')
        else:
            bag[item_id] = {'skates_by_size': {skate_size: quantity}}
            messages.success(request, f'Added {product.name} size\
                             {skate_size.upper()} to your bag')

    elif clothes_size:
        if item_id in list(bag.keys()):
            if clothes_size in bag[item_id]['clothes_by_size'].keys():
                bag[item_id]['clothes_by_size'][clothes_size] += quantity
                messages.success(request, f'Updated {product.name} size\
                                 {clothes_size.upper()} quantity to\
                                 {bag[item_id]["clothes_by_size"][clothes_size]}')
            else:
                bag[item_id]['clothes_by_size'][clothes_size] = quantity
                messages.success(request, f'Added {product.name} size\
                                 {clothes_size.upper()} to your bag')
        else:
            bag[item_id] = {'clothes_by_size': {clothes_size: quantity}}
            messages.success(request, f'Added {product.name} size\
                             {clothes_size.upper()} to your bag')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to\
                             {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Change the quantity of a product in the bag"""
    bag = request.session.get('bag', {})

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    skate_size = request.POST.get('bag_skate_size')
    clothes_size = request.POST.get('bag_clothes_size')

    if skate_size:
        if quantity > 0:
            bag[item_id]['skates_by_size'][skate_size] = quantity
            messages.success(request, f'Updated {product.name} size\
                             {skate_size.upper()} quantity to\
                             {bag[item_id]["skates_by_size"][skate_size]}')
        else:
            del bag[item_id]['skates_by_size'][skate_size]
            if not bag[item_id]['skates_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} size\
                                 {skate_size.upper()} from your bag')

    elif clothes_size:
        if quantity > 0:
            bag[item_id]['clothes_by_size'][clothes_size] = quantity
            messages.success(request, f'Updated {product.name} size\
                             {clothes_size.upper()} quantity to\
                             {bag[item_id]["clothes_by_size"][clothes_size]}')
        else:
            del bag[item_id]['clothes_by_size'][clothes_size]
            if not bag[item_id]['clothes_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} size\
                                 {clothes_size.upper()} from your bag')

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to\
                             {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove a product from the bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        skate_size = request.POST.get('bag_skate_size')
        clothes_size = request.POST.get('bag_clothes_size')

        if skate_size:
            del bag[item_id]['skates_by_size'][skate_size]
            if not bag[item_id]['skates_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} size\
                                 {skate_size.upper()} from your bag')

        elif clothes_size:
            del bag[item_id]['clothes_by_size'][clothes_size]
            if not bag[item_id]['clothes_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} size\
                                 {clothes_size.upper()} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
