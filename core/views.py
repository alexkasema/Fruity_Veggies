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

def category_product_fruits_view(request):

    fruits = Product.objects.filter(category__title = "Fruits")

    context = {'fruits': fruits}
    return render(request, 'core/category_fruits_list.html', context)