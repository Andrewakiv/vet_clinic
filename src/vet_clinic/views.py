from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import ModelFormMixin

from accounts.models import StaffProfile
from .forms import TestimonialAddForm, OrderForm, CommentForm
from .models import Service, Post, Category, Testimonial, Order
from .utils import DataMixin


class HomeView(DataMixin, ListView):
    context_object_name = 'services_list'
    template_name = 'vet_clinic/index.html'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Home')


class ServicesView(DataMixin, ListView):
    context_object_name = 'services_list'
    template_name = 'vet_clinic/services.html'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Services')


class ServiceDetailView(DataMixin, ModelFormMixin, DetailView):
    # model = Service
    template_name = 'vet_clinic/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'service_slug'  # from url
    form_class = OrderForm

    def get_object(self, queryset=None):
        return get_object_or_404(Service, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['service'].title)

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.service = self.get_object()
            new_order.name = request.user
            new_order.save()
            return redirect('vet_clinic:services')


class BlogView(DataMixin, ListView):
    context_object_name = 'posts'
    template_name = 'vet_clinic/blog.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Blog')


class BlogDetailView(DataMixin, ModelFormMixin, DetailView):
    template_name = 'vet_clinic/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'blog_slug'
    form_class = CommentForm

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comm_post.filter(active=True)  # check related name
        return self.get_mixin_context(context, title=context['post'].title)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.get_object()
            new_comment.name = request.user
            new_comment.save()
            return redirect('vet_clinic:blog_detail', blog_slug=self.kwargs[self.slug_url_kwarg])


@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')

    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Post.DoesNotExists:
            pass
    return JsonResponse({'status': 'error'})


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


@permission_required("order.view_order")
def show_orders(request):
    orders = Order.objects.all()
    services_list = Service.objects.all()

    data = {
        'orders': orders,
        'services_list': services_list
    }

    return render(request, 'vet_clinic/orders.html', context=data)


@permission_required("order.view_order")
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    data = {
        'order': order
    }

    return render(request, 'vet_clinic/order-detail.html', context=data)


@permission_required("order.view_order")
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = Order.Status.COMPLETE
        order.save()
        messages.success(request, "Order has been completed")
        return redirect('vet_clinic:order_detail', order_id=order_id)
    else:
        data = {
            'order': order
        }

    return render(request, 'vet_clinic/order-detail.html', context=data)


@permission_required("order.view_order")
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = Order.Status.CONFIRM
        order.save()
        messages.success(request, "Order has been confirmed")
        return redirect('vet_clinic:order_detail', order_id=order_id)
    data = {
        'order': order
    }

    return render(request, 'vet_clinic/order-detail.html', context=data)


@permission_required("order.view_order")
def delay_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = Order.Status.DELAY
        order.save()
        messages.warning(request, "Order has been postponed")
        return redirect('vet_clinic:order_detail', order_id=order_id)
    data = {
        'order': order
    }

    return render(request, 'vet_clinic/order-detail.html', context=data)


@permission_required("order.view_order")
def show_filter_orders(request, service_slug):
    orders = Order.objects.filter(service__slug=service_slug)

    data = {
        'orders': orders,
    }

    return render(request, 'vet_clinic/orders.html', context=data)


@permission_required("order.view_order")
def draft_orders(request):
    orders = Order.objects.filter(status=Order.Status.DRAFT)

    data = {
        'orders': orders,
    }

    return render(request, 'vet_clinic/orders.html', context=data)


@permission_required("order.view_order")
def completed_orders(request):
    orders = Order.objects.filter(status=Order.Status.COMPLETE)

    data = {
        'orders': orders,
    }

    return render(request, 'vet_clinic/orders.html', context=data)


@permission_required("order.view_order")
def confirmed_orders(request):
    orders = Order.objects.filter(status=Order.Status.CONFIRM)
    services_list = Service.objects.all()
    data = {
        'orders': orders,
        'services_list': services_list
    }

    return render(request, 'vet_clinic/orders.html', context=data)


@permission_required("order.view_order")
def delayed_orders(request):
    orders = Order.objects.filter(status=Order.Status.DELAY)

    data = {
        'orders': orders,
    }

    return render(request, 'vet_clinic/orders.html', context=data)


def show_user_orders(request, user_username):
    user_order = get_object_or_404(User, username=user_username)
    orders = Order.objects.filter(name=user_order)

    data = {
        'user_order': user_order,
        'orders': orders
    }

    return render(request, 'vet_clinic/user_orders.html', context=data)


def contacts(request):
    return render(request, 'vet_clinic/contacts.html')


def about(request):
    staff = StaffProfile.objects.all()

    data = {
        'staff': staff,
        'default_profile': settings.DEFAULT_PROFILE_IMAGE
    }

    return render(request, 'vet_clinic/about-us.html', context=data)
