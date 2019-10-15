from django import template

register = template.Library()


@register.simple_tag
def get_cover_photo_url(product_obj, model_number):
    return product_obj.get_cover_photo(model_number).image_file.url
