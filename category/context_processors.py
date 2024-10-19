from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links) # now will will loop through over links
