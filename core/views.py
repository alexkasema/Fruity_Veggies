from django.shortcuts import render

from . models import Product, Category, Vendor

# Create your views here.

def index(request):

    products = Product.objects.filter(product_status = "published", featured = True)
    category_v = Category.objects.filter(title = "Vegetables")
    vegetables = Product.objects.filter(category__title = "Vegetables")
    fruits = Product.objects.filter(category__title = "Fruits")
    categories = Category.objects.all()

    context = {
        'products': products, 'categories': categories, 'vegetables': vegetables, 'fruits': fruits
    }
    return  render(request, 'core/index.html', context)

def product_list_view(request):

    products = Product.objects.filter(product_status = "published", featured=True)
    vegetables = Product.objects.filter(category__title = "Vegetables")
    fruits = Product.objects.filter(category__title = "Fruits")

    context = {
        'products': products, 'vegetables': vegetables, 'fruits': fruits
    }
    return render(request, 'core/product_list.html', context)

def product_details_view(request, pid):

    product = Product.objects.get(pid=pid)
    vegetables = Product.objects.filter(category__title = "Vegetables")
    fruits = Product.objects.filter(category__title = "Fruits")

    context = {
        'product': product, 'fruits': fruits, 'vegetables': vegetables
    }

    return render(request, 'core/product_details.html', context)

def category_product_fruits_view(request):

    fruits = Product.objects.filter(category__title = "Fruits")

    context = {'fruits': fruits}
    return render(request, 'core/category_fruits_list.html', context)

def category_product_vegetables_view(request):

    vegetables = Product.objects.filter(category__title = "Vegetables")

    context = {'vegetables': vegetables}
    return render(request, 'core/category_vegetables_list.html', context)

def vendors_list_view(request):

    vendors = Vendor.objects.all()

    context = {
        'vendors': vendors
    }
    return render(request, 'core/vendors_list.html', context)

def vendor_details_view(request, vid):

    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status = "published")

    context = {
        'vendor': vendor, 'products': products
    }
    return render(request, 'core/vendor_details.html', context)

