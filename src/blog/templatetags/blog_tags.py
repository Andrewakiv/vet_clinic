from django import template

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/category_blog.html')
def category_blog_tag():
    categories = Category.objects.all()
    return {'categories': categories}
