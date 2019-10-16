from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    color = models.CharField(max_length=30, blank=True)
    model_number = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE, blank=True)
    power = models.CharField(max_length=100, blank=True)
    capacity = models.CharField(max_length=20, blank=True)
    certificate = models.CharField(max_length=100, blank=True)
    accessory = models.CharField(max_length=255, blank=True)
    fob = models.CharField(max_length=30, blank=True)
    cif = models.CharField(max_length=30, blank=True)
    product_dimension = models.CharField(max_length=30, blank=True)
    giftbox_dimension = models.CharField(max_length=30, blank=True)
    master_carton_dimension = models.CharField(max_length=30, blank=True)
    net_weight = models.CharField(max_length=30, blank=True)
    gross_weight = models.CharField(max_length=30, blank=True)
    cap_20gp = models.PositiveIntegerField(blank=True, null=True)
    cap_40gp = models.PositiveIntegerField(blank=True, null=True)
    cap_40hq = models.PositiveIntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_cover_photo(cls, model_number):
        product = cls.objects.get(model_number=model_number)
        cover_photo = product.photos.all()[0]
        return cover_photo

    def __str__(self):
        return self.title


def photo_directory_path(instance, filename):
    return 'product_photos/model_{0}/{1}'.format(instance.product.model_number, filename)


class ProductPhoto(models.Model):
    product = models.ForeignKey(
        Product, related_name="photos", on_delete=models.CASCADE)
    image_file = models.FileField(upload_to=photo_directory_path)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.image_file.name
