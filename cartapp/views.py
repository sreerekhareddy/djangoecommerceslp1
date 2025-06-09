from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from catalog.models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    # Use product_id as a string key
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart  # 🟢 Save back into session
    return redirect(view_cart)

'''
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cartapp/view_cart.html', {'cart_items': cart_items})
'''

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity
        })

    return render(request, 'cart/cart.html', {'cart_items': cart_items})



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id_str = str(product_id)
    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]  # Remove item completely if quantity becomes 0

        request.session['cart'] = cart  # Save back

    return redirect(view_cart)

'''
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Try to get an existing cart item
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')
    
    
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        cart_item = CartItem.objects.get(user=request.user, product=product)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()  # Quantity is 1, so remove the item completely

    except CartItem.DoesNotExist:
        pass  # Ignore if item not found

    return redirect('view_cart')
    
    '''