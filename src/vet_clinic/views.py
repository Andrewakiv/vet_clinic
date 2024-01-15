from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TestimonialAddForm
from .models import Service, Post, Category, Testimonial


def home(request):
    services_list = Service.objects.all()

    data = {
        'services_list': services_list,
        'default_service': settings.DEFAULT_USER_IMAGE
    }

    return render(request, 'vet_clinic/index.html', context=data)


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

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    data = {
        'posts': posts,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/blog.html', context=data)


def blog_detail(request, blog_slug):
    post = get_object_or_404(Post, slug=blog_slug)

    data = {
        'post': post,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/blog_detail.html', context=data)


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
    responses_list = Testimonial.objects.all()

    paginator = Paginator(responses_list, 6)
    page_number = request.GET.get('page', 1)
    responses_list = paginator.page(page_number)

    if request.method == 'POST':
        form = TestimonialAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vet_clinic:responses')
    else:
        form = TestimonialAddForm()

    data = {
        'responses_list': responses_list,
        'form': form,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/responses.html', context=data)


def contacts(request):
    return HttpResponse('contacts')

