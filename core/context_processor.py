from . models import Product, Category, Vendor, WishList

from django.db.models import Min, Max

def default(request):
    
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    try:
        wishlist = WishList.objects.filter(user=request.user)
    except:
        
        wishlist = 0

    return {
        'categories': categories, 'vendors': vendors, 'min_max_price': min_max_price,'wishlist': wishlist
    }