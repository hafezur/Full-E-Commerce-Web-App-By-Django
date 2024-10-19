from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
#from cart.models import CartItem
from django.db.models import Q

#from cart.views import _cart_id
from django.core.paginator import Paginator # this for paginations


def store(request, category_slug=None):
    categories = Category.objects.all()
    products = None  # product initially nao thakte pare

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
    }
    return render(request, 'store/store.html', context)

from .models import CommentAndReview
from .forms import commentAndReviewForm
from orders.models import Order
def product_detail(request, category_slug, product_slug):
    comment='xyz'
    ratting=0
    average_rating=0
    if request.method =='POST':
        form=commentAndReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.cleaned_data['write_comment']
            ratting=form.cleaned_data['ratings']
            print("PAKISTAN PAKISTAN PAKISTAN PAKISTAN PAKISTAN PAKISTAN")
            print(comment)
        else:
            pass
    else:
        form = commentAndReviewForm()
    if comment != 'xyz':
        curent=request.user
        print(curent)
        user=Account.objects.get(email=curent)
        user_name1=user.first_name
        user_image=user.pro_picture
        print(user_name1)
        user_addres1=[]
        find_order=Order.objects.all()
        order_counter=find_order.count()
        if order_counter >0:
            real_add=Order.objects.filter(user=curent)
            loop_flag=0
            for x in real_add:
                if loop_flag == 0:
                    user_addres1.append(x.address_line1)
                    user_addres1.append(x.address_line2)
                    user_addres1.append(x.city)
                loop_flag +=1
        rating_count=0
        total_rating_value=0
        all_ratings=CommentAndReview.objects.filter(comment_slug=product_slug)
        all_ratings_count=CommentAndReview.objects.filter(comment_slug=product_slug).count()
        if all_ratings_count > 0:
            for x in all_ratings:
                total_rating_value+=x.ratings
                rating_count+=1
            
            average_rating = total_rating_value/all_ratings_count
            print("AVERAGE")
            print(average_rating)
        else:
            average_rating=ratting    
                
        CommentAndReview.objects.create(
            comment_slug = product_slug,
            write_comment =comment,
            user_name     = user_name1,
            user_address  = user_addres1,
            ratings       = ratting,
            user_photo =user_image,
            avg_ratings=average_rating,
        )
    #CommentAndReview.save()
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) #category__slug= Product ar sathe category ar akta somporkho acc ,,many to one tai double(__) user kora hoyasa.
        #print("AVERAGE1")
        #print(single_product.specific_product.avg_ratings)
#         in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
         raise e
    wish_based_single_product=Product.objects.all()
    all_comment=CommentAndReview.objects.filter(comment_slug=product_slug)
    total_comment_number=CommentAndReview.objects.filter(comment_slug=product_slug).count()
    total_comment_sum=0
    if total_comment_number> 0:
        for x in all_comment:
            print(x.avg_ratings)
            total_comment_sum+=x.avg_ratings
        print(total_comment_sum)
        print(total_comment_number)
        average_rating=total_comment_sum/total_comment_number
    else:
        pass 
    comment='xyz'
    context = {
         'single_product': single_product,
         'form'       : form,
         'wish_based_single_product':wish_based_single_product,
         'all_comment': all_comment,
         'comment':comment,
         'average_rating':average_rating,
     }
    return render(request, 'store/product_details.html', context)


def search(request): # this is for searching.
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count() # Q= when use multiple logical filter in model we will ues Q. and icontains= case insensetive
    context = {
        'products': products,
        'p_count': product_count,
    }
    return render(request, 'store/store.html', context)


from accounts.models import Account
from . models import OrderRequest
from django.http import HttpResponse
def Order_request(request):
    pre_order=OrderRequest.objects.all()
    user=Account.objects.get(email=request.user) # here user means  login email address.
    Customer_name=user.first_name
    product_name='abc'
    product_quentity=0
    if request.method =='POST':
        product_name=request.POST.get('Product_name'),
        product_quentity=request.POST.get('Quentity'),
        address=request.POST.get('Address'),
        Company_Name=request.POST.get('Company_Name'),
        Aspected_delivery_date=request.POST.get('Aspected_delivery_date')
    if product_quentity==0:
        pass
    else:
        product_name1=str(product_name[0])
        product_quentity1=str(product_quentity[0])
        product_quentity2=int(product_quentity1)
        get_all_product_name=Product.objects.all()
        final_name='xyz'
        single_price=0
        for name in get_all_product_name:
            value=name.product_name
            value1=value
            pp=name.price
            if value1 == product_name1:
                final_name=product_name1
                single_price=pp
                pro_image=name.images
            else:
                pass

        final_price=product_quentity2*single_price       
        if final_name =='xyz':
            indicator='Invalid Product Name! Please select Valid Product name.'
            pre_order=OrderRequest.objects.all()
            count=pre_order.count()
            context={
                'indicator':indicator,
                'pre_order':pre_order,
                'count':count,
            }
            return render(request,'store/offline_oder.html',context)
        
        print(final_name)
        order_request=OrderRequest(
            customer_name=Customer_name,
            product_name=product_name,
            product_quentity=product_quentity2,
            price=final_price,
            product_image=pro_image,
            address=address,
            company_name=Company_Name,
            aspected_date=Aspected_delivery_date,
        
        )
        order_request.save()
    all_order_request=OrderRequest.objects.all()
    count=all_order_request.count()
    context={
        'all_order':all_order_request,
        'count':count,
        'pre_order':pre_order,
    }
    return render(request,'store/offline_oder.html',context)

def Cancel_order(request,id):
    all_order=OrderRequest.objects.all()
    order=OrderRequest.objects.filter(pk=id)
    print(order.product_name)
    context={
        'all_order':all_order,
    }
    return render(request,'store/offline_oder.html',context)
    

def comment_and_review(request,category_slug,product_slug):
    comment='bismillah'
    if request.method =='POST':
        form=commentAndReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.cleaned_data['write_comment']
            print("PAKISTAN PAKISTAN PAKISTAN PAKISTAN PAKISTAN PAKISTAN")
            print(comment)
        else:
            pass
    else:
        form = commentAndReviewForm()
    return render(request,'store/product_details.html')