from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)  # if url name= Blue Tshirt --> slug make this --> blue-tshirt , so slug make lowercase and create a hifen between two words.
    description = models.TextField(max_length=255, blank=True)  
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)  # ami jodi akta picture add kori tahola media/photos/categories ar moddha save hobe..

    class Meta: # extra characteristics added, 
        verbose_name = 'category'  # ai name ta backend a dakhabe---> for singlar
        verbose_name_plural = 'categories'  # ai name ta backend a dakhabe---> for plural
    def get_url(self):
        return reverse('products_by_category', args=[self.slug]) # this is for making urls for context_processors
    def __str__(self): 
        return self.category_name 

