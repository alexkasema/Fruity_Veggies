from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),

    #! category
    path('fruits', views.category_product_fruits_view, name="fruits"),
]