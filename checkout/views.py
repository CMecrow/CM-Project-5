from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LYneYJcdUfLFdWTD1kkcf1xygNkBj9djxe0lYMowwt4kDQPTo734VmmwNiAdCL7Q1qqyEQENHLqzsIJpNWHdKkh00zUWrx0ZX',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
