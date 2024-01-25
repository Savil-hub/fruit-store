from django.shortcuts import render, redirect
from .models import Purchase
from .forms import PurchaseForm
from fruits.models import Product 
from django.contrib.auth.decorators import login_required


def product_list(request):
    # Retrieve a list of products and display them to the user
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def checkout(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Create a purchase record
            purchase = form.save(commit=False)
            purchase.user = request.user  # Assign the logged-in user
            purchase.save()

            # Additional logic for payment processing can be added here

            # Clear the user's cart after the purchase
            request.session['cart'] = {}

            # Redirect to a purchase success page
            return redirect('purchase_success')
    else:
        form = PurchaseForm()

    return render(request, 'buy/checkout.html', {'form': form})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Initialize the cart in the session if it doesn't exist
    cart = request.session.get('cart', {})

    # Check if the product is already in the cart
    if product_id in cart:
        # Increment the quantity if the product is already in the cart
        cart[product_id]['quantity'] += 1
    else:
        # Add the product to the cart with quantity 1
        cart[product_id] = {'quantity': 1, 'name': product.name, 'price': product.price}

    # Update the cart in the session
    request.session['cart'] = cart

    return redirect('buy:product_list')


@login_required
def item_detail(request, item_id):
    # Your view logic here
    return render(request, 'buy/item_detail.html', {'item_id': item_id})


@login_required
def order_confirmation(request):
    # Your view logic here
    return render(request, 'buy/order_confirmation.html')