from django.shortcuts import get_object_or_404, redirect, render

from ..forms import PhotoForm
from ..models import Category, Product


def category_photos(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all().order_by('-created_at')
    return render(request, 'products/category_photos.html', {'category': category, 'products': products})


def product_photos(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = get_object_or_404(Product, pk=product_id)
    photos = product.photos.all().order_by('-created_at')
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(product)
            return redirect('products:product_photos', category_id, product_id)
    else:
        form = PhotoForm()
    return render(request, 'products/product_photos.html',
                  {'form': form, 'category': category, 'product': product, 'photos': photos})
