from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Schedule
from vet_clinic.models import Service


class ShowOrders(PermissionRequiredMixin, ListView):
    context_object_name = 'orders'
    template_name = 'pet_care_scheduler/orders.html'
    permission_required = 'pet_care_scheduler.view_schedule'

    def get_queryset(self):
        return Schedule.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_list'] = Service.objects.all()
        return context


class OrderDetail(PermissionRequiredMixin, DetailView):
    model = Schedule
    template_name = 'pet_care_scheduler/order-detail.html'
    context_object_name = 'order'
    slug_url_kwarg = 'order_id'
    permission_required = 'pet_care_scheduler.view_schedule'

    def get_object(self, queryset=None):
        return get_object_or_404(Schedule, id=self.kwargs[self.slug_url_kwarg])



class CompleteOrder(View):
    template_name = 'pet_care_scheduler/order-detail.html'

    def get(self, request, order_id):
        order = get_object_or_404(Schedule, id=order_id)
        context = {'order': order}
        return render(request, self.template_name, context)

    def post(self, request, order_id):
        order = get_object_or_404(Schedule, id=order_id)
        order.status = Schedule.Status.COMPLETE
        order.save()
        messages.success(request, "Order has been completed")
        return redirect('schedule:order_detail', order_id=order_id)


class ConfirmOrder(View):
    template_name = 'pet_care_scheduler/order-detail.html'

    def get(self, request, order_id):
        order = get_object_or_404(Schedule, id=order_id)
        context = {'order': order}
        return render(request, self.template_name, context)

    def post(self, request, order_id):
        order = get_object_or_404(Schedule, id=order_id)
        order.status = Schedule.Status.CONFIRM
        order.save()
        messages.success(request, "Order has been completed")
        return redirect('schedule:order_detail', order_id=order_id)

class DelayOrder(View):
    template_name = 'pet_care_scheduler/order-detail.html'

    def get(self, request, order_id):
        order = get_object_or_404(Schedule, id=order_id)
        context = {'order': order}
        return render(request, self.template_name, context)

    def post(self, request, order_id):
        order = get_object_or_404(Schedule, id=order_id)
        order.status = Schedule.Status.DELAY
        order.save()
        messages.success(request, "Order has been completed")
        return redirect('schedule:order_detail', order_id=order_id)


class FilterOrders(ListView):
    template_name = 'pet_care_scheduler/orders.html'
    context_object_name = 'orders'

    def get_queryset(self, queryset=None):
        service_slug = self.kwargs.get('service_slug')
        return Schedule.objects.filter(service__slug=service_slug)


class DraftOrders(ListView):
    template_name = 'pet_care_scheduler/orders.html'
    context_object_name = 'orders'

    def get_queryset(self, queryset=None):
        return Schedule.objects.filter(status=Schedule.Status.DRAFT)


class CompletedOrders(ListView):
    template_name = 'pet_care_scheduler/orders.html'
    context_object_name = 'orders'

    def get_queryset(self, queryset=None):
        return Schedule.objects.filter(status=Schedule.Status.COMPLETE)


class ConfirmedOrders(ListView):
    template_name = 'pet_care_scheduler/orders.html'
    context_object_name = 'orders'

    def get_queryset(self, queryset=None):
        return Schedule.objects.filter(status=Schedule.Status.CONFIRM)


class DelayedOrders(ListView):
    template_name = 'pet_care_scheduler/orders.html'
    context_object_name = 'orders'

    def get_queryset(self, queryset=None):
        return Schedule.objects.filter(status=Schedule.Status.DELAY)


class UserOrders(ListView):
    template_name = 'pet_care_scheduler/user_orders.html'

    def get_queryset(self, queryset=None):
        user_username = self.kwargs.get('user_username')
        user_order = get_object_or_404(get_user_model(), username=user_username)
        return Schedule.objects.filter(name=user_order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_username = self.kwargs.get('user_username')
        context['orders'] = self.get_queryset()
        context['user_order'] = get_object_or_404(get_user_model(), username=user_username)
        return context
