from django.shortcuts import get_object_or_404, render

from ..models import Category, Product


def category_photos(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    return render(request, 'products/category_photos.html', {'category': category, 'products': products})


def product_photos(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = get_object_or_404(Product, pk=product_id)
    photos = product.photos.all()
    return render(request, 'products/product_photos.html', {'category': category, 'product': product, 'photos': photos})
