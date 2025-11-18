from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin): # Admin panel customize korte model admin use kori.
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)} # this is for slug functions
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.OrderRequest)
admin.site.register(models.CommentAndReview)