from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Category)
class CategoryAdmin(admin.ModelAdmin): # In this portion ModelAdmin is used , causes when we want to edit admin interface , we have to use model admin.
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(models.Category, CategoryAdmin) 