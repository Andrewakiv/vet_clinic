from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView

from .forms import TestimonialAddForm
from .models import Service, Post, Category, Testimonial


class HomeView(ListView):
    model = Service
    context_object_name = 'services_list'
    template_name = 'vet_clinic/index.html'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['default_service'] = settings.DEFAULT_USER_IMAGE
        return context


def about(request):
    return HttpResponse('about')


class ServicesView(ListView):
    model = Service
    context_object_name = 'services_list'
    template_name = 'vet_clinic/services.html'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Services'
        context['default_service'] = settings.DEFAULT_USER_IMAGE
        return context


class ServiceDetailView(DetailView):
    # model = Service
    template_name = 'vet_clinic/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'service_slug'  # from url

    def get_object(self, queryset=None):
        return get_object_or_404(Service.objects, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['service'].title
        context['default_service'] = settings.DEFAULT_USER_IMAGE
        return context


class BlogView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'vet_clinic/blog.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['default_service'] = settings.DEFAULT_USER_IMAGE
        return context


class BlogDetailView(DetailView):
    # model = Post
    template_name = 'vet_clinic/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'blog_slug'  # from url

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['default_service'] = settings.DEFAULT_USER_IMAGE
        return context


def category_blog(request, category_blog_slug):
    category = get_object_or_404(Category, slug=category_blog_slug)
    posts = Post.objects.filter(category_id=category.pk).select_related('category')

    data = {
        'posts': posts,
        'default_service': settings.DEFAULT_USER_IMAGE
    }
    return render(request, 'vet_clinic/blog.html', context=data)


class CategoryBlogView(ListView):
    model = Category
    template_name = 'vet_clinic/blog.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        # category_slug from its url
        return Post.objects.filter(category__slug=self.kwargs['category_blog_slug']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['posts'].first().category  # from queryset first item then its category
        context['title'] = 'Category - ' + category.name  # name from category
        return context



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

