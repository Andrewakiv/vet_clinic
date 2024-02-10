from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Schedule


class ScheduleForm(forms.ModelForm):
    date_for_visit = forms.DateField(widget=forms.widgets.DateInput(attrs={'class': 'contacts-form__input-service',
                                                                           'type': 'date'}))

    class Meta:
        model = Schedule
        fields = ['phone_number', 'pet_info', 'date_for_visit']
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'form-control'}, initial='UA'),
            'pet_info': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Pet's name and age"}),
        }