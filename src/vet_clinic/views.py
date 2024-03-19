import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin

from accounts.models import StaffProfile
from actions.utils import create_action
from pet_care_scheduler.forms import ScheduleForm
from .forms import TestimonialAddForm
from .models import Service, Testimonial
from .utils import DataMixin


logger = logging.getLogger('vet_clinic')


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
    form_class = ScheduleForm

    def get_object(self, queryset=None):
        return get_object_or_404(Service, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['service'].title)

    def post(self, request, *args, **kwargs):
        form = ScheduleForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.service = self.get_object()
            new_order.name = request.user
            new_order.save()
            # create_action(request.user, 'makes order', new_order)
            logger.info(f'{request.user.username} has made an order')
            return redirect('vet_clinic:services')


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
            logger.info(f'{request.user.username} response')
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
    return render(request, 'vet_clinic/contacts.html')


def about(request):
    staff = get_user_model().objects.filter(groups__name='doctors')

    data = {
        'staff': staff,
        'default_profile': settings.DEFAULT_PROFILE_IMAGE
    }

    return render(request, 'vet_clinic/about-us.html', context=data)
