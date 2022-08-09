from django.shortcuts import render
# Create your models here.


def view_bag(request):
    """A view to return the shopping bag"""

    return render(request, 'bag/bag.html')
