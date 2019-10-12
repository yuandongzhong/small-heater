from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('photos/', views.product_photos, name='product_photos'),
]
