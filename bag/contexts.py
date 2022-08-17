from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """Context processor to make bag contents available across the project"""

    bag_items = []
    total = 0
    product_count = 0
    clothes_size_key = 'clothes_by_size'
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        elif clothes_size_key in item_data.keys():
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['clothes_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['skates_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                type(item_data)
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_COST:
        delivery = settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_COST - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context