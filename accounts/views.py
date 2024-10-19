from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout






# varification mail:
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from cart.views import _cart_id
from cart.models import Cart,CartItem
#from .import request

def register(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=email.split("@")[0] # suppose email = rahim-khan@gamil.com , the username is rahim-khan, from @ here split, means bad daoya hoyasa.
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password) # this create_user exits in model here.
            user.phone_number=phone_number
            user.save()
            
            # USER ACTIVATION
            current_site=get_current_site(request) # current domain ta nilam such as http://127.0.0.1:8000/
            mail_subject='Please activate your account'
            message=render_to_string('accounts/account_verification_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), # for every user a single id has create.
                'token':default_token_generator.make_token(user), # user ar data ar upor base kore token create hossa.
            }) # here , html template dila seta string a convert hoya jabe. so the functionality of render_to_string is this.
            to_email=email
            print(type(to_email))
            print(to_email)
            send_email=EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request,'Thank you for registering with us. We have sent you a verification email to your email address please verify it.')
            return redirect('/accounts/initial_registration/login/?command=verification&email=' +email) # command =verificatin na diya onno kiso o daoya jate pare.. 
    else:
        form =RegistrationForm()
    context={'form':form,}
    return render (request,'accounts/register.html',context)


# def login(request):
#     if request.method =='POST':
#         email=request.POST['email'] # post field thaka email ta nilam
#         password=request.POST['password'] ## post field thaka password ta nilam
#         user=auth.authenticate(email=email,password=password) # authenticate korer korer jonno eamil and password user ar jonno patalam
#         if user is not None:
#             auth.login(request,user)
#             return redirect('dashboard')
#         else:
#             messages.error(request,'Invalid login credentials')
#             return redirect('login')
#     return render(request,'accounts/login.html') 
 


def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode() # decode means human redable from of uid
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user =None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Congratulations! Your account is activated. ')
        return redirect('login')
    else:
        messages.error(request,'Invalid activation link ')
        return redirect('register')
    

from orders.models import Payment
@login_required(login_url='login')
def dashboard(request):
    last_order=Order.objects.latest('created_at')
    payment=Payment.objects.latest('created_at')
    top_products=Product.objects.filter(stock=0)
    context={
        'last_order':last_order,
        'payment':payment,
        'top_products':top_products,
    }
    return render(request,'accounts/dashboard.html', context )

def sales_report(request):
    products=Product.objects.all()
    item_sold=[]
    for x in products:
        initial_stock=x.product_capacity
        current_stock=x.stock
        current_product=initial_stock-current_stock
        pro_name=x.product_name
        dic={
            'current_stock':current_stock,
            'current_product':current_product,
            'pro_name':pro_name,
        }
        item_sold.append(dic)
    context={
        'products':products,
        'item_sold':item_sold,
    }
    return render(request, 'sub_dashboard/sales_statictics_and_report.html',context)

from orders.models import OrderedProduct
def all_transaction(request):
    all_tran=OrderedProduct.objects.all()
    all_tran_pay=Payment.objects.all()
    context={
        'all_tran':all_tran,
        'all_tran_pay':all_tran_pay,
    }
    return render(request,'sub_dashboard/transactions.html',context)

def delete_transaction(request,id):
    all_tran=Payment.objects.get(id=id)
    all_tran.delete()
    all_tran_pay=Payment.objects.all()
    context={
        'all_tran_pay':all_tran_pay,
    }
    return render(request,'sub_dashboard/transactions.html',context)

def all_category(request):
    all_item=Category.objects.all()
    context={
        'all_item':all_item,
    }
    return render (request,'sub_dashboard/all_category.html',context)

def top_selling_product(request):
    top_products=Product.objects.filter(stock=0)
    context={
        'top_products':top_products,
    }
    return render (request,'sub_dashboard/top_selling_product.html',context)


def forgotPassword(request):
    if request.method =='POST':
        email=request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)
            #Reset password email
            current_site=get_current_site(request)
            mail_subject='Reset Your Pssword'
            message=render_to_string('accounts/reset_password_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            sent_email=EmailMessage(mail_subject, message, to=[to_email])
            sent_email.send()
            
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request,'Account does not exist!')
            return redirect('forgotPassword')
    return render(request,'accounts/forgotPassword.html')
                        

def resetpassword_validate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid 
        messages.success(request,'Please reset your password')
        return redirect("resetPassword")
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password == confirm_password:
            uid=request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    return render(request,'accounts/resetPassword.html')              


@login_required(login_url='login')
def user_logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out. ')
    return redirect('login')







def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        user=auth.authenticate(email=email,password=password)
        
        if user is not None:
            try:
                cart=Cart.objects.get(cart_id=_cart_id(request))
                print("here is cart:",type(cart))
                is_cart_item_exists=CartItem.objects.filter(cart=cart).exists()
                print
                if is_cart_item_exists:
                    cart_item=CartItem.objects.filter(cart=cart)
                    
                    # getting the product variations by cart id:
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                    #get the cart items from the user to access his product variations
                    cart_item=CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)
                    # product_variation =[1,2,3,4,5]
                    #ex_var_list =[4,6,3,5]
                    
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index=ex_var_list.index(pr)
                            item_id=id[index]
                            item=CartItem.objects.get(id=item_id)
                            item.quantity +=1
                            item.user=user
                            item.save()
                        else:
                            cart_item=CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user=user
                                item.save()
            except:
                pass
            auth.login(request,user)
            messages.success(request,'You are now logged in. ')
            url=request.META.get('HTTP_REFERER')
            try:
                query=request.utils.urlparse(url).query
                # next=/cart/checkout
                params=dict(x.spit('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage=params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')


# @login_required(login_url='login')
# def Delete_account(request):
#         print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#         deteleUser=Account.objects.filter(email=email, )
#         deteleUser.delete()
#         auth.logout(request)
#         return redirect('login')
@login_required(login_url='login')
def select_account(request):
    return render(request,'accounts/delete_account.html')


@login_required(login_url='login')
def Delete_account(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from POST data
        
        if email:
            try:
                deteleUser = Account.objects.get(email=email)
                deteleUser.delete()
                auth.logout(request)
                return redirect('login')
            except Account.DoesNotExist:
                # Handle the case where the account with the provided email does not exist
                return render(request, 'accounts/error.html', {'message': 'Account not found.'})
        else:
            # Handle the case where email is not provided
            return render(request, 'accounts/error.html', {'message': 'Email not provided.'})
    
    return render(request, 'accounts/login.html')

def select_your_registration(request):
    return render(request,'accounts/initialRegistration.html')

def select_your_login(request):
    return render(request,'accounts/initialLogin.html')

# def profileManagement(request):
#     picture=Account.objects.all()
#     get_pic=picture.picture
#     print(get_pic)
#     return render(request,'accounts/profile_management.html')

from django.shortcuts import render
from .models import Account

def profileManagement(request):
    # Fetch all Account objects
    accounts = Account.objects.all()
    active_accounts = Account.objects.filter(is_active=True)
    #pictures = [account.picture.url if account.picture else None for account in accounts]

    for acc in active_accounts:
        first_name=acc.first_name
        email=acc.email
        if acc.pro_picture:
            picture=acc.pro_picture
    #print("kdfjkedjf",picture)

    return render(request, 'accounts/profile_management.html', {'picture': picture})

from .models import Account
from django.http import HttpResponse
from .forms import ImageUploadForm
def profilePicUpload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Assuming you have a way to get the current user or account instance
            # For example, if the user is logged in:
            email = request.user.email
            account = Account.objects.get(email=email)  # Adjust this query as needed

            # Update the `pro_picture` field with the uploaded image
            account.pro_picture = form.cleaned_data['image']
            account.save()  # Save the updated account instance

            # Optionally, redirect or send a success message
            return redirect('profile_management')
    else:
        form = ImageUploadForm()

    return render(request, 'accounts/profile_management.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

@login_required
def update_personal_info(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            # Assuming you have a way to get the current user or account instance
            # For example, if the user is logged in:
            email = request.user.email
            account = Account.objects.get(email=email)  # Adjust this query as needed

            # Update the `pro_picture` field with the uploaded image
            account.first_name =form.cleaned_data['first_name']
            account.last_name =form.cleaned_data['last_name']
            account.email =form.cleaned_data['email']
            account.username =form.cleaned_data['username']
            account.phone_number =form.cleaned_data['phone_number']
            account.save()  # Save the updated account instance

            # Optionally, redirect or send a success message
            return redirect('profile_management')
    else:
        form = ProfileUpdateForm()

    return render(request, 'accounts/update_personal_info.html', {'form': form})

from .forms import AddressUpdateForm
from orders.models import Order
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddressUpdateForm


@login_required
def manage_user_address(request):
    if request.method == 'POST':
        form = AddressUpdateForm(request.POST)
        if form.is_valid():
            user = request.user
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            try:
                # Fetch the order associated with the user
                orders = Order.objects.filter(user=user)
            except Order.DoesNotExist:
                # Handle the case where the order does not exist
                return redirect('error_page')  # Redirect to an error page or handle the error appropriately

            # Update the order with the new address details
            for order in orders:
                order.address_line1 = form.cleaned_data['address_line1']
                order.city = form.cleaned_data['city']
                order.state = form.cleaned_data['state']
                order.country = form.cleaned_data['country']
                order.save() 

            # Optionally, redirect or send a success message
            return redirect('profile_management')
    else:
        form = AddressUpdateForm()

    return render(request, 'accounts/user_address.html', {'form': form})

def go_to_Wish_list(request):
    all_wish_list_product=WishListProduct.objects.all()
    context={
        'all_wish_list_product':all_wish_list_product
    }
    return render(request, 'wish_list/wish_list_Product.html',context)



from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from django.db.models import Q
from django.core.paginator import Paginator # this for paginations


def Get_product_for_wish_list(request, category_slug=None):
    categories = Category.objects.all()
    products = None  # product initially nao thakte pare
    wish_list_products=[]
    previous_wish_products=WishListProduct.objects.all()
    for x in previous_wish_products:
        wish_list_products.append(x.wish_product_name)
    if category_slug != None: # jodi page ar specific category thake.
        category= get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        
        paginator = Paginator(products, 3) # (products, 3) = products is some objects, if category slug exist then i will show 3 product in every page.
        page = request.GET.get('page') #currently kon  page a ace. in detail from backend which page number had sent and it recieve that page number.
        paged_products = paginator.get_page(page) 
        
        product_count = products.count() 
    else: # jodi page ar specific category na thake.
        products = Product.objects.filter(is_available=True)
        
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        product_count = products.count()
        

    context = {
        'products': paged_products,
        'p_count': product_count,
        'categories':categories,
        'wish_list_products':wish_list_products,
    }
    return render(request, 'wish_list/products_for_wish_list.html', context)

from .models import WishListProduct
def add_to_wish_list(request, product_slug):
    wish_product=Product.objects.get(slug=product_slug)
    wish_product.is_wish=True
    wish_product.save()
    product_name=wish_product.product_name
    product_price=wish_product.price
    product_image=wish_product.images
    product_description=wish_product.description
    product_id=wish_product.pk
    #print(product_id)
    pp_name='xyz'
    wish_id=WishListProduct.objects.all()
    for x in wish_id:
        if x.wish_product_slug == product_slug:
            pp_name=x.wish_product_slug
    
    if(pp_name != product_slug):
        WishListProduct.objects.create(
            id=product_id,
            wish_product_slug=product_slug,
            wish_product_name=product_name,
            wish_product_price=product_price,
            wish_product_image=product_image,
            wish_product_description=product_description,
        )
    specific_wish_products=WishListProduct.objects.all()
        
    context={
            'specific_wish_products':specific_wish_products
        }
    print("HERE WISHLIST BY BY")
    return render(request, 'wish_list/wish_list_Product.html',context)
    
from store.models import OrderRequest
def see_order_request(request):
    all_order=OrderRequest.objects.all()
    count=all_order.count()
    context={
        'all_order':all_order,
        'count':count,
    }
    return render(request,'sub_dashboard/all_requested_order.html',context)

def delete_requested_order(request,id):
    order=OrderRequest.objects.filter(pk=id)
    order.delete()
    all_order=OrderRequest.objects.all()
    context={
        'all_order':all_order,
    }
    return render(request,'sub_dashboard/all_requested_order.html',context)
   

