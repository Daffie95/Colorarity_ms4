from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IdA8fJBuBWM0lqnHjgDevg6Qaw2TrILkgfPQm6q081v2zHuM0RnoXpRclO5E4As33NiYIHomLY1IfQNLwgdfCb900Ygjmagbp',
        'client_secret_key': 'sk_test_51IdA8fJBuBWM0lqnZW1F4YegLU76ClYxVthDaIwVJVn3QwrsDULgO4tKzSZu2isGn2AFV0ZE1zt0Nze0qHcupnMz00wmnp8AA1'

    }

    return render(request, template, context)
