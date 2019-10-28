from django import forms
from PIL import Image

from .models import Category, Product, ProductPhoto


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'title',
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
        labels = {
            'title': '标题',
            'description': '其他描述',
            'price': '价格',
            'color': '颜色',
            'model_number': '型号*',
            'category': '品类',
            'power': '功率',
            'capacity': '容积',
            'certificate': '认证',
            'accessory': '配件',
            'fob': 'FOB价格',
            'cif': 'CIF价格',
            'product_dimension': '产品尺寸',
            'giftbox_dimension': '彩箱尺寸',
            'master_carton_dimension': '外箱尺寸',
            'net_weight': '净重',
            'gross_weight': '毛重',
            'cap_20gp': '20GP容量',
            'cap_40gp': '40GP容量',
            'cap_40hq': '40HQ容量',
            'is_available': '是否在售'}


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = ProductPhoto
        fields = ('image_file', 'x', 'y', 'width', 'height', )
        labels = {
            'image_file': '产品图片',
        }

    def save(self, product, user):
        photo = super(PhotoForm, self).save(commit=False)
        photo.product = product
        photo.created_by = user
        photo.save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.image_file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((600, 600), Image.ANTIALIAS)
        resized_image.save(photo.image_file.path)
        return photo
