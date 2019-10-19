from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.utils import timezone

from .forms import CategoryForm, ProductForm
from .models import Category, Product


def home(request):
    categories = Category.objects.order_by('-created_at').annotate(
        number_of_products=Count('products'))
    return render(request, 'home.html', {'categories': categories})


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    return render(request, 'products/category_products.html', {'category': category, 'products': products})


def save_category_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            categories = Category.objects.order_by('-created_at').annotate(
                number_of_products=Count('products'))
            data['html_category_list'] = render_to_string(
                'products/includes/partial_category_list.html', {
                    'categories': categories
                })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    else:
        form = CategoryForm()
    return save_category_form(request, form, 'products/includes/partial_category_create.html')


def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
    else:
        form = CategoryForm(instance=category)
    return save_category_form(request, form, 'products/includes/partial_category_update.html')


def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    data = dict()
    if request.method == 'POST':
        category.delete()
        data['form_is_valid'] = True
        categories = Category.objects.order_by('-created_at').annotate(
            number_of_products=Count('products'))
        data['html_category_list'] = render_to_string('products/includes/partial_category_list.html', {
            'categories': categories
        })
    else:
        context = {'category': category}
        data['html_form'] = render_to_string('products/includes/partial_category_delete.html',
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


def save_product_form(request, category_id, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            product = form.save()
            product.updated_at = timezone.now()
            product.save()
            data['form_is_valid'] = True
            products = Product.objects.order_by('-updated_at')
            data['html_product_list'] = render_to_string(
                'products/includes/partial_product_list.html', {
                    'categories': products
                })
        else:
            data['form_is_valid'] = False
    context = {'category_id': category_id, 'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def product_create(request, category_id):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    return save_product_form(request, category_id, form, 'products/includes/partial_product_create.html')
