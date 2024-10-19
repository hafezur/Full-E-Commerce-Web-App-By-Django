from django.db import models
from store.models import Product
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True) 
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # One to many relationShip , such as ..akta cart er akta item a eki  product different size ar hoita pare
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True) # One to many relationShip , such as ..akta curt a onakgolo cart_item thakte pare.
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        if self.product.have_dis>0:
            val_sub_total=self.product.discount_price() * self.quantity
        else:
            val_sub_total=self.product.price * self.quantity
        return val_sub_total # price calculation

    def __self__(self):
        return self.product
