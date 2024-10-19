from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key # try to getting session key
    if not cart: # if session does't exists 
        cart = request.session.create() # create a session key using a function (create())
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) # get an object of Product model using primary key(id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the Cart model object using session_key.
    except Cart.DoesNotExist: # if Cart model object does't exists creat it.
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart) # get the objects of CartItem model using Product model and Cart model
        cart_item.quantity  += 1
        cart_item.save()
    except CartItem.DoesNotExist: # if CartItem model objects does not exists , create it.
        cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
        cart.save()
    return redirect('cart')
        

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            if cart_item.product.have_dis>0:
                total += (cart_item.product.discount_price() * cart_item.quantity)
            else:
                total += (cart_item.product.price * cart_item.quantity)
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)


def remove_cart(request, product_id, cart_item_id): # this function is used for decreasing cart items.

    product = get_object_or_404(Product, id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id): #
    product = get_object_or_404(Product, id=product_id)
    
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

