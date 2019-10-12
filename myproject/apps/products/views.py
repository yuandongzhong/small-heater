from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def product_list(request):
    return render(request, 'products/product_list.html')


def product_photos(request):
    return render(request, 'products/product_photos.html')
