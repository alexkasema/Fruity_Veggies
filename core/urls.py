from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),

    #! products view
    path('products', views.product_list_view, name="products"),
    path('product/<pid>', views.product_details_view, name="product"),

    #! category
    path('fruits', views.category_product_fruits_view, name="fruits"),
    path('vegetables', views.category_product_vegetables_view, name="vegetables"),

    #! vendor
    path('vendors', views.vendors_list_view, name="vendors"),
    path('vendor/<vid>', views.vendor_details_view, name="vendor"),

     #! tags
    path('products/tags/<slug:tag_slug>', views.tag_list_view, name="tags"),

    #! add reviews
    path('reviews/<pid>/', views.review_form_view, name="reviews"),

    #! Search by product title
    path('search/', views.search_products_view, name="search_products"),

    #! filter products by category, vendor
    path('filter_products/', views.filter_products_view, name="filter_products"),
]