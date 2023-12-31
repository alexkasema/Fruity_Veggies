from django.urls import path, include

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

    #! add product to cart
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),

    #! cart page
    path('cart', views.cart_view, name="cart"),

    #! delete-item-from-cart
    path('delete-from-cart', views.delete_item_from_cart, name="delete-from-cart"),

    #! update cart
    path('update-cart', views.update_cart, name="update-cart"),

    #! Checkout url
    path('checkout', views.checkout_view, name="checkout"),

    #! paypal url
    path('paypal/', include('paypal.standard.ipn.urls')),

    #! payment completed url
    path('payment-completed', views.payment_completed_view, name="payment-completed"),

    #! payment failed url
    path('payment-failed', views.payment_failed_view, name="payment-failed"),

    #! dashboard url
    path('dashboard/', views.dashboard_view, name="dashboard"),

    #! order details url
    path('dashboard/order/<int:id>', views.order_detail_view, name="order-details"),

    #! making address default url
    path('make-default-address', views.make_address_default_view, name="make-default-address"),

    #! adding to wishlist url
    path('add-to-wishlist', views.add_to_wishlist_view, name="add-to-wishlist"),

    #! wishlist view url
    path('wishlist', views.wishlist_view, name="wishlist"),

    #! removing from wishlist view url
    path('remove-from-wishlist', views.remove_from_wishlist, name="remove-from-wishlist"),

    #! contact view url
    path('contact', views.contact_view, name="contact"),

    #! ajax contact view url
    path('ajax-contact-form', views.ajax_contact, name="ajax-contact-form"),
]