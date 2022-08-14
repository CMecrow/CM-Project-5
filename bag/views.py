from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
# Create your models here.


def view_bag(request):
    """A view to return the shopping bag"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the selected product to the shopping bag"""

    product = Product.objects.get(pk=item_id)
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
            print(bag)
            if skate_size in list(bag[item_id]['skates_by_size'].keys()):
                bag[item_id]['skates_by_size'][skate_size] += quantity
            else:
                bag[item_id]['skates_by_size'][skate_size] = quantity
        else:
            bag[item_id] = {'skates_by_size': {skate_size: quantity}}

    elif clothes_size:
        if item_id in list(bag.keys()):
            if clothes_size in bag[item_id]['clothes_by_size'].keys():
                bag[item_id]['clothes_by_size'][clothes_size] += quantity
            else:
                bag[item_id]['clothes_by_size'][clothes_size] = quantity
        else:
            bag[item_id] = {'clothes_by_size': {clothes_size: quantity}}

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Change the quantity of a product in the bag"""
    bag = request.session.get('bag', {})

    quantity = int(request.POST.get('quantity'))
    skate_size = request.POST.get('bag_skate_size')
    clothes_size = request.POST.get('bag_clothes_size')

    if skate_size:
        if quantity > 0:
            bag[item_id]['skates_by_size'][skate_size] = quantity
        else:
            del bag[item_id]['skates_by_size'][skate_size]
            if not bag[item_id]['skates_by_size']:
                bag.pop(item_id)

    elif clothes_size:
        if quantity > 0:
            bag[item_id]['clothes_by_size'][clothes_size] = quantity
        else:
            del bag[item_id]['clothes_by_size'][clothes_size]
            if not bag[item_id]['clothes_by_size']:
                bag.pop(item_id)

    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove a product from the bag"""
    try:
        bag = request.session.get('bag', {})
        skate_size = request.POST.get('bag_skate_size')
        clothes_size = request.POST.get('bag_clothes_size')

        if skate_size:
            del bag[item_id]['skates_by_size'][skate_size]
            if not bag[item_id]['skates_by_size']:
                bag.pop(item_id)

        elif clothes_size:
            del bag[item_id]['clothes_by_size'][clothes_size]
            if not bag[item_id]['clothes_by_size']:
                bag.pop(item_id)

        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


    # if 'skate_size' in request.POST:
    #     skate_size = request.POST['skate_size']

    # clothes_size = None

    # if 'clothes_size' in request.POST:
    #     clothes_size = request.POST['clothes_size']
        

    # if skate_size:
    #     if quantity > 0:
    #         bag[item_id]['skates_by_size'][skate_size] = quantity
    #     else:
    #         del bag[item_id]['skates_by_size'][skate_size]

    # elif clothes_size:
    #     if quantity > 0:
    #         bag[item_id]['clothes_by_size'][clothes_size] = quantity
    #     else:
    #         del bag[item_id]['clothes_by_size'][clothes_size]