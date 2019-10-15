from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('categories/<int:category_id>/',
         views.category_products, name='category_products'),
    path('categories/<int:category_id>/photos/',
         views.category_photos, name='category_photos'),
    path('categories/<int:category_id>/photos/<int:product_id>/',
         views.product_photos, name='product_photos'),
]