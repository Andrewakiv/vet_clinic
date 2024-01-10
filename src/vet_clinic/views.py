from django.http import HttpResponse
from django.shortcuts import render

from .models import Service


def home(request):
    services_list = Service.objects.all()
    return render(request, 'vet_clinic/index.html', {'services_list': services_list})


def about(request):
    return HttpResponse('about')


def services(request):
    services_list = Service.objects.all()
    return render(request, 'vet_clinic/services.html', {'services_list': services_list})


def faq(request):
    return HttpResponse('faq')


def responses(request):
    return HttpResponse('responses')


def contacts(request):
    return HttpResponse('contacts')


def blog(request):
    return HttpResponse('blog')
