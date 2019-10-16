from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .forms import CategoryForm
from .models import Category, Product


def home(request):
    categories = Category.objects.annotate(
        number_of_products=Count('products'))
    return render(request, 'home.html', {'categories': categories})


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    return render(request, 'products/category_products.html', {'category': category, 'products': products})


def category_create(request):
    data = dict()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            categories = Category.objects.annotate(
                number_of_products=Count('products'))
            data['html_category_list'] = render_to_string(
                'products/includes/partial_category_list.html', {
                    'categories': categories
                })
        else:
            data['form_is_valid'] = False
    else:
        form = CategoryForm()

    context = {'form': form}
    data['html_form'] = render_to_string(
        'products/includes/partial_category_create.html',
        context,
        request=request)
    return JsonResponse(data)


def category_photos(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    return render(request, 'products/category_photos.html', {'category': category, 'products': products})


def product_photos(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = get_object_or_404(Product, pk=product_id)
    photos = product.photos.all()
    return render(request, 'products/product_photos.html', {'category': category, 'product': product, 'photos': photos})
