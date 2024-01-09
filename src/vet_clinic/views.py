from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'vet_clinic/index.html')


def about(request):
    return HttpResponse('about')


def services(request):
    return HttpResponse('services')


def faq(request):
    return HttpResponse('faq')


def responses(request):
    return HttpResponse('responses')


def contacts(request):
    return HttpResponse('contacts')
