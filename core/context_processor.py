from . models import Product, Category, Vendor

def default(request):
    
    categories = Category.objects.all()

    return {
        'categories': categories
    }