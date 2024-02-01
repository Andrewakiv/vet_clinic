from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Schedule
from vet_clinic.models import Service


@permission_required('pet_care_scheduler.view_schedule')
def show_orders(request):
    orders = Schedule.objects.all()
    services_list = Service.objects.all()

    data = {
        'orders': orders,
        'services_list': services_list
    }

    return render(request, 'pet_care_scheduler/orders.html', context=data)


@permission_required('pet_care_scheduler.view_schedule')
def order_detail(request, order_id):
    order = get_object_or_404(Schedule, id=order_id)

    data = {
        'order': order
    }

    return render(request, 'pet_care_scheduler/order-detail.html', context=data)


def complete_order(request, order_id):
    order = get_object_or_404(Schedule, id=order_id)
    if request.method == 'POST':
        order.status = Schedule.Status.COMPLETE
        order.save()
        messages.success(request, "Order has been completed")
        return redirect('schedule:order_detail', order_id=order_id)
    else:
        data = {
            'order': order
        }

    return render(request, 'pet_care_scheduler/order-detail.html', context=data)


def confirm_order(request, order_id):
    order = get_object_or_404(Schedule, id=order_id)
    if request.method == 'POST':
        order.status = Schedule.Status.CONFIRM
        order.save()
        messages.success(request, "Order has been confirmed")
        return redirect('schedule:order_detail', order_id=order_id)
    data = {
        'order': order
    }

    return render(request, 'pet_care_scheduler/order-detail.html', context=data)


def delay_order(request, order_id):
    order = get_object_or_404(Schedule, id=order_id)
    if request.method == 'POST':
        order.status = Schedule.Status.DELAY
        order.save()
        messages.warning(request, "Order has been postponed")
        return redirect('schedule:order_detail', order_id=order_id)
    data = {
        'order': order
    }

    return render(request, 'pet_care_scheduler/order-detail.html', context=data)


def show_filter_orders(request, service_slug):
    orders = Schedule.objects.filter(service__slug=service_slug)

    data = {
        'orders': orders,
    }

    return render(request, 'pet_care_scheduler/orders.html', context=data)


def draft_orders(request):
    orders = Schedule.objects.filter(status=Schedule.Status.DRAFT)

    data = {
        'orders': orders,
    }

    return render(request, 'pet_care_scheduler/orders.html', context=data)


def completed_orders(request):
    orders = Schedule.objects.filter(status=Schedule.Status.COMPLETE)

    data = {
        'orders': orders,
    }

    return render(request, 'pet_care_scheduler/orders.html', context=data)


def confirmed_orders(request):
    orders = Schedule.objects.filter(status=Schedule.Status.CONFIRM)
    services_list = Service.objects.all()
    data = {
        'orders': orders,
        'services_list': services_list
    }

    return render(request, 'pet_care_scheduler/orders.html', context=data)


def delayed_orders(request):
    orders = Schedule.objects.filter(status=Schedule.Status.DELAY)

    data = {
        'orders': orders,
    }

    return render(request, 'pet_care_scheduler/orders.html', context=data)


def show_user_orders(request, user_username):
    user_order = get_object_or_404(get_user_model(), username=user_username)
    orders = Schedule.objects.filter(name=user_order)

    data = {
        'user_order': user_order,
        'orders': orders
    }

    return render(request, 'pet_care_scheduler/user_orders.html', context=data)


