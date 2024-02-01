from django.contrib import admin
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Schedule


class OrderForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(),
        }


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'pet_info', 'service', 'order_date', 'date_for_visit']
    list_display_links = ['id', 'name']
    ordering = ['-order_date', 'name']
    search_fields = ['name', 'pet_info']
    form = OrderForm
