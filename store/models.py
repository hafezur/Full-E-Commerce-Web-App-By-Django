from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class CommentAndReview(models.Model):
    #specific_product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    comment_slug =models.SlugField(max_length=1000, unique=False, blank=True)
    write_comment=models.TextField(max_length=1000, blank=True)
    user_name    =models.CharField(max_length=100,blank=True)
    user_photo   =models.ImageField(null=True)
    user_address =models.CharField(max_length=100,blank=True)
    comment_date =models.DateTimeField(auto_now_add=True)
    ratings      =models.FloatField(blank=True,null =True)
    avg_ratings  =models.FloatField(blank=True,null =True)
    def __str__(self): # (def__str__(self), In admin interface Product model shows by product_name. check it.
        return self.comment_slug

class Product(models.Model):
    specific_product=models.ForeignKey(CommentAndReview,on_delete=models.CASCADE,null=True,blank=True)
    product_name    = models.CharField(max_length=200, unique=True) # product name must unique
    slug            = models.SlugField(max_length=200, unique=True) # convert product name as lowercase and create hifen between two name
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products') # image path
    stock           = models.IntegerField() # how many number is present in stock
    product_capacity=models.IntegerField(default=100, editable=True)
    is_available    = models.BooleanField(default=True) # is product available or not.
    is_wish         =models.BooleanField(default=False)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE) # ForeignKey is used for meantain One to Many relation ship,here have a one to many relation btwn Product model and Category model.
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    have_dis        =models.IntegerField(default=False)

    def __str__(self): # (def__str__(self), In admin interface Product model shows by product_name. check it.
        return self.product_name

    def get_url(self): # causes of uses this functions = amra jokhon product_name click korbo tokhon product_details show korbe and url hisabe first a category slug/product slug jabe.
        return reverse('product_detail', args=[self.category.slug, self.slug]) 
    def discount_price(self):
        dis_price=(self.have_dis/100)*self.price
        original=round(self.price-dis_price)
        return original
    
class OrderRequest(models.Model):
    customer_name=models.CharField(max_length=50)
    product_name=models.CharField(max_length=50)
    product_quentity=models.IntegerField()
    price=models.IntegerField()
    product_image=models.ImageField()
    address=models.CharField(max_length=50)
    company_name=models.CharField(max_length=100)
    aspected_date=models.DateField()
    is_accept=models.BooleanField(default=True)


    
        
    
   