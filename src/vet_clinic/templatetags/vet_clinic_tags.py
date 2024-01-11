from django import template

from vet_clinic.models import Category

register = template.Library()


@register.inclusion_tag('vet_clinic/category_blog.html')
def category_blog_tag():
    categories = Category.objects.all()
    return {'categories': categories}
