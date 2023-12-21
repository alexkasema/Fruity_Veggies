from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from django.template.loader import render_to_string

from . models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address

from . forms import ProductReviewForm

from taggit.models import Tag

from django.contrib import messages #! for flash messages

from django.db.models import Avg, Count
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
    products = Product.objects.filter(category=product.category).exclude(pid=pid) #![:4] at the end to show first 4

    vegetables = Product.objects.filter(category__title = "Vegetables")
    fruits = Product.objects.filter(category__title = "Fruits")
    #!get all reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    #! getting average reviews
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    #! product review form
    review_form = ProductReviewForm()

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False
    
    

    context = {
        'product': product, 'products':products ,'fruits': fruits, 'vegetables': vegetables,
        'reviews': reviews, 'average_rating': average_rating, 'review_form': review_form,
        'make_review': make_review
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

def tag_list_view(request, tag_slug=None):

    products = Product.objects.filter(product_status = "published")
    vegetables = Product.objects.filter(category__title = "Vegetables")
    fruits = Product.objects.filter(category__title = "Fruits")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        'products': products, 'tag': tag, 'vegetables': vegetables, 'fruits': fruits
    }

    return render(request, 'core/tag.html', context)

def review_form_view(request, pid):
    
    product = Product.objects.get(pid=pid)
    user = request.user

    review = ProductReview.objects.create(
        user = user,
        product = product,
        review = request.POST.get('review'),
        rating = request.POST.get('rating'),
    )

    context = {
        'user': user.username,
        'review': request.POST.get('review'),
        'rating': request.POST.get('rating'),
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews,
        }
    )