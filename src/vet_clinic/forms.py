from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Testimonial, Order, Comment
from django.utils.text import slugify


class TestimonialAddForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'response', 'is_published']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'contacts-form__input-name', 'placeholder': 'Enter your full name'}),
            'response': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'class': 'contacts-form__input-response',
                                              'placeholder': "Enter your response"})
        }

    def save(self, commit=True):
        instance = super(TestimonialAddForm, self).save(commit=False)
        instance.slug = slugify(instance.name)

        if commit:
            instance.save()
        return instance


class OrderForm(forms.ModelForm):
    date_for_visit = forms.DateField(widget=forms.widgets.DateInput(attrs={'class': 'contacts-form__input-service',
                                                                           'type': 'date'}))

    class Meta:
        model = Order
        fields = ['phone_number', 'pet_info', 'date_for_visit']
        widgets = {
            # 'name': forms.TextInput(
            #     attrs={'class': 'contacts-form__input-name', 'placeholder': 'Enter your full name'}),
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'contacts-form__input-service'}, initial='UA'),
            'pet_info': forms.TextInput(
                attrs={'class': 'contacts-form__input-pets-info', 'placeholder': "Pet's name and age"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comm_content']
        widgets = {
            'comm_content': forms.Textarea(attrs={'cols': 10, 'rows': 1, 'class': 'contacts-form__input-response',
                                                  'placeholder': "Enter your response"})
        }
