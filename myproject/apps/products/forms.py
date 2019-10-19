from django import forms

from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title',
                  'description',
                  'price',
                  'color',
                  'model_number',
                  'category',
                  'power',
                  'capacity',
                  'certificate',
                  'accessory',
                  'fob',
                  'cif',
                  'product_dimension',
                  'giftbox_dimension',
                  'master_carton_dimension',
                  'net_weight',
                  'gross_weight',
                  'cap_20gp',
                  'cap_40gp',
                  'cap_40hq',
                  'is_available')
