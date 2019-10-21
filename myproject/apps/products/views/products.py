from django import forms
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.utils import timezone

from ..forms import ProductForm
from ..models import Category, Product


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all().order_by('-updated_at')
    return render(request, 'products/category_products.html', {'category': category, 'products': products})


def save_product_form(request, category_id, form, template_name, is_category_hidden):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            category = get_object_or_404(Category, pk=category_id)
            product = form.save(commit=False)
            if is_category_hidden:
                product.category = category
            product.updated_at = timezone.now()
            product.save()
            data['form_is_valid'] = True
            products = category.products.all().order_by('-updated_at')
            # products = Product.objects.filter(
            #     category=category).order_by('-updated_at')
            data['html_product_list'] = render_to_string(
                'products/includes/partial_product_list.html', {
                    'category': category,
                    'products': products
                })
        else:
            data['form_is_valid'] = False
    context = {'category_id': category_id,
               'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def product_create(request, category_id):
    request_path = request.get_full_path()
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    form.fields['category'].widget = forms.HiddenInput()
    return save_product_form(request,
                             category_id,
                             form,
                             'products/includes/partial_product_create.html',
                             is_category_hidden=True)


def product_update(request, category_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
    else:
        form = ProductForm(instance=product)
    return save_product_form(request,
                             category_id,
                             form,
                             'products/includes/partial_product_update.html',
                             is_category_hidden=False)
