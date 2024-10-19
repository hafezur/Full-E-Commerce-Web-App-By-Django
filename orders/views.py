from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart,CartItem
from .forms import OrderForm,OrderMakeForm
from .ssl import sslcommerz_payment_gateway
from .models import Payment, OrderedProduct, Order
from store.models import Product
# Create your views here.
from .ssl import sslcommerz_payment_gateway
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from accounts.models import Account,WishListProduct
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from accounts.models import MyAccountManager,Account
from accounts.views import activate,register
from django.contrib.auth import authenticate
# Create your views here.
def _cart_id(request):
    cart = request.session.session_key # try to getting session key
    if not cart: # if session does't exists 
        cart = request.session.create() # create a session key using a function (create())
    return cart

@csrf_exempt # csrf ke disable kore deoya
def success_view(request):
    data = request.POST
    print('data -------', data)
    print('HAFIZ........', data["amount"])
    #user_id = int(data['value_b']) # Retrieve the stored user ID as an integer
    user_id = int(data['value_b']) # Retrieve the stored user ID as an integer
    user = Account.objects.get(pk=user_id)
    print('OOOOOOOOO ,,,,, USER: ',user)
    payment = Payment(
        user = user,
        payment_id =data['tran_id'],
        payment_method = data['card_issuer'],
        amount_paid = int(data['store_amount'][0]),
        status =data['status'],
    )
    payment.save()
    total_order_obj=Order.objects.count()
    print("HA HA HA HA HA ")
    print(total_order_obj)
    # working with order model
    #order = Order.objects.get(user=user, is_ordered=False, order_number=data['value_a'])
    #print(type(data['value_a']))
    fist=data['value_a']
    #print(data['value_a'])
    if total_order_obj < 2:
        find_order_number=1
        order = Order.objects.get(user=user, is_ordered=False, order_number=find_order_number)
    else:
        find_order=Order.objects.all().last()
        find_order_number=find_order.id
        print(find_order_number)
        print("TRY TRY TRY TRY TRY  TRY TRY TRY TRY TRY TRY TRY TRY TRY TRY")
        order = Order.objects.get(user=user, is_ordered=False, order_number=find_order_number)
    order.is_ordered = True
    order.save() 
    
    cart_items = CartItem.objects.all()
    
    
    for item in cart_items:
        orderproduct = OrderedProduct()
        product = Product.objects.get(id=item.product.id)
        orderproduct.order = order
        orderproduct.payment = payment
        orderproduct.user = user
        orderproduct.product = product
        orderproduct.quantity = item.quantity
        orderproduct.ordered = True
        orderproduct.save()

        # Reduce the quantity of the sold products
        
        product.stock -= item.quantity # order complete tai stock theke quantity komay dilam
        product.save()

    # Clear cart
    CartItem.objects.all().delete()
    paid_amount=data["amount"]
    transaction_date=data["tran_date"]
    paid_by=data["card_issuer"]
    risk_title=data["risk_title"]
    status=data["status"]
    context={
        'paid_amount':paid_amount,
        'transaction_date':transaction_date,
        'paid_by':paid_by,
        'risk_title':risk_title,
        'status':status,
    }
    return render(request,'orders/invoice.html',context)

# def place_order(request, total=0, quantity=0, cart_items=None):
#     #print(request.POST)
#     try:
#         tax = 0
#         grand_total = 0
        
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, is_active=True)
#         if cart_items.count() < 1:
#             return redirect('store')
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#         tax = (2 * total)/100
#         grand_total = total + tax
#         if request.method == 'POST':
#             form = OrderForm(request.POST)
#             if form.is_valid():
#                 form.instance.user = request.user
#                 form.instance.order_total = grand_total
#                 form.instance.tax = tax
#                 form.instance.ip = request.META.get('REMOTE_ADDR')
#                 form.instance.payment = 2
#                 saved_instance = form.save()  # Save the form data to the database
#                 form.instance.order_number = saved_instance.id
            
#                 form.save()
#                 print('form print', form)
#                 return redirect(sslcommerz_payment_gateway(request,  saved_instance.id, str(request.user.id), grand_total))
#     except ObjectDoesNotExist:
#         pass #just ignore

#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax'       : tax,
#         'grand_total': grand_total,
#     }
#     return render(request,'orders/place-order.html', context)

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        wish_product_slug_list=[] # wishList delete or product is_wish func
        # Assuming you have a Cart and CartItem model
        cart = Cart.objects.get(cart_id=_cart_id(request))
        print(cart.cart_id)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        get_imediate_last_object = Order.objects.all().last()
        if get_imediate_last_object:
            get_imediate_last_object_id=(get_imediate_last_object.id) + 1
        else:
            get_imediate_last_object_id=1
        print(get_imediate_last_object_id)
        print(type(get_imediate_last_object_id))
        
        if cart_items.count() < 1:
            return redirect('store')
        
        for cart_item in cart_items:
            value=cart_item.product
            value.is_wish=False
            value.save()
            cart_item.product.is_wish=False # wishList delete or product is_wish func
            
            cart_item.save() # wishList delete or product is_wish func
            wish_product_slug_list.append(cart_item.product.slug) # wishList delete or product is_wish func
            product_x = cart_item.product
            total += (product_x.price * cart_item.quantity)
        
        tax = (2 * total) / 100
        grand_total = total + tax
        
        wish_product=WishListProduct.objects.all() # wishList delete or product is_wish func
        # wishList delete or product is_wish func start
        for wish in wish_product: 
            wish_slug=wish.wish_product_slug
            for cart_slug in wish_product_slug_list:
                product_slug=cart_slug
                if wish_slug == product_slug:
                    wish_item=WishListProduct.objects.get(wish_product_slug=product_slug)
                    wish_item.delete()
        # wishList delete or product is_wish func end        
        #collect_product_name_or_names
        name_array=[]
        for xx in cart_items:
            name=xx.product.product_name
            name_array.append(name)
        print("NAME NAME NAME NAME NAME NAME NAME NAME NAME NAME NAME NAME NAME ")
        for yy in name_array:
            print(yy)
        if request.method == 'POST':
            first_name = request.POST.get('first_name')          
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone_number')
            
            # product_name = request.POST.get('product_name')
            # try:
            #     # Find the Product instance by name
            #     product = Product.objects.get(product_name=product_name)
            # except Product.DoesNotExist:
            #     # Handle the case where the product does not exist
            #     product = None
            #     # Optionally, you might want to show an error message to the user
            #     return render(request, 'orders/place-order.html', {'error': 'Product does not exist'})
            
            address_line1 = request.POST.get('address_line1')
            address_line2 = request.POST.get('address_line2')
            state = request.POST.get('state')
            city = request.POST.get('city')
            country = request.POST.get('country')
            order_note = request.POST.get('order_note')
            
            # Create and save the Order instance
            order = Order(
                user=request.user,
                order_number=get_imediate_last_object_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                find_product_name=name_array,  # Assign the Product instance
                address_line1=address_line1,
                address_line2=address_line2,
                state=state,
                city=city,
                country=country,
                order_note=order_note,
                order_total=grand_total,
                tax=tax
            )
            
            # Save the Order instance to the database
            order.save()
            get_id=order.id
            print(get_id)
            # Redirect or handle success
            
            return redirect(sslcommerz_payment_gateway(request, order.id,  str(request.user.id), grand_total))

    except ObjectDoesNotExist:
        # Handle cases where cart or cart items are not found
        return redirect('store')

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'orders/place-order.html', context)



def order_complete(request):
    return render(request,'orders/order_complete.html')

# def invoice(request):
#     data = request.POST
#     report_value=data["amount"]
#     context={
#         'report_value':report_value,
#     }
#     return render(request,'orders/invoice.html',context)
    
# def order_history(request):
#     orders=Order.objects.all()
#     print(orders.first_name)
#     return render(request,'orders/order_history.html')

from django.shortcuts import render

def order_history(request):
    user=request.user
    ordered_products = Order.objects.filter(user=user)

    order_info_list = []  # List to hold dictionaries with order information
    find_order_quentiry=OrderedProduct.objects.filter(user=user)
    total_payment=Payment.objects.filter(user=user)
    
    print(find_order_quentiry)
    amount_list=[]
    size_of_amount_list=range(len(amount_list))
    size_of_order_info_list=range(len(order_info_list))

    for ordered_product in ordered_products:
        order_info = {
            'first_name': ordered_product.first_name,
            'last_name': ordered_product.last_name,
            'email': ordered_product.email,
            'phone': ordered_product.phone,
            'state': ordered_product.state,
            'city': ordered_product.city,
            'country': ordered_product.country,
            'tax': ordered_product.tax,
            #'product_name':ordered_product.find_product_name.product_name,
            #'product_category':ordered_product.find_product_name.category.category_name,
            'amount_paid':ordered_product.order_total,
            'order_number':ordered_product.order_number,
            'address_line1':ordered_product.address_line1,
            'address_line2':ordered_product.address_line2,
            'order_note':ordered_product.order_note,
            'order_total':ordered_product.order_total,
            'created_at':ordered_product.created_at,
        }
        
        # Append the dictionary to the list
        order_info_list.append(order_info)
        print(order_info_list)
        

    context = {
        'order_info_list': order_info_list,
        'ordered_products':ordered_products, # Pass the list of order info dictionaries to the template
    }
    print("HUM HUM HUM HUM HUM HUM HUM HUM HUM HUM HUM")
    print(order_info_list)
    return render(request, 'orders/order_history.html', context)

# def order_history(request):
    
#     user=request.user
#     ordered_products = Order.objects.filter(user=user)
#     print(ordered_products)

#     return render(request, 'accounts/order_history.html',{'ordered_products':ordered_products})

from django.shortcuts import render
from .models import Order

def recent_order(request):
    # Get the most recent order
    recent = Order.objects.latest('created_at')  # Assuming 'created_at' is the field to sort by
    return render(request, 'orders/recent_order.html', {'recent_order': recent})



from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Order

def order_delete(request, id):
    product = Order.objects.get(id=id)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(product.order_number)
    product.delete()
    user=request.user
    ordered_products = Order.objects.filter(user=user)
    context={
        'ordered_products':ordered_products,
    }
    return render(request, 'orders/order_history.html', context)

    