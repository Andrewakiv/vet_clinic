from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Service, Post


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


def faq(request):
    return HttpResponse('faq')


def responses(request):
    return HttpResponse('responses')


def contacts(request):
    return HttpResponse('contacts')

