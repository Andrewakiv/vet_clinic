from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Service, Post, Category


def home(request):
    services_list = Service.objects.all()
    return render(request, 'vet_clinic/index.html', {'services_list': services_list})


def about(request):
    return HttpResponse('about')


def services(request):
    services_list = Service.objects.all()
    data = {
        'services_list': services_list,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/services.html', context=data)


def service_detail(request, service_slug):
    service = get_object_or_404(Service, slug=service_slug)

    data = {
        'service': service,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/service_detail.html', context=data)


def blog(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/blog.html', context=data)


def category_blog(request, category_blog_slug):
    category = get_object_or_404(Category, slug=category_blog_slug)
    posts = Post.objects.filter(category_id=category.pk).select_related('category')

    data = {
        'posts': posts,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/blog.html', context=data)


def faq(request):
    return HttpResponse('faq')


def responses(request):
    return HttpResponse('responses')


def contacts(request):
    return HttpResponse('contacts')

