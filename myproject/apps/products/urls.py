from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('categories/create/',
         views.category_create, name='category_create'),
    path('categories/<int:category_id>/update/',
         views.category_update, name='category_update'),
    path('categories/<int:category_id>/delete/',
         views.category_delete, name='category_delete'),
    path('categories/<int:category_id>/',
         views.category_products, name='category_products'),
    path('categories/<int:category_id>/photos/',
         views.category_photos, name='category_photos'),
    path('categories/<int:category_id>/photos/<int:product_id>/',
         views.product_photos, name='product_photos'),
    path('categories/<int:category_id>/create/',
         views.product_create, name='product_create'),
]
