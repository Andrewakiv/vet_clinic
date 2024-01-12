from django import forms
from .models import Testimonial
from django.utils.text import slugify


class TestimonialAddForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'response', 'is_published']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contacts-form__input-name', 'placeholder': 'Enter your full name'}),
            'response': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'class': 'contacts-form__input-response',
                                              'placeholder': "Enter your response"})
        }

    def save(self, commit=True):
        instance = super(TestimonialAddForm, self).save(commit=False)
        instance.slug = slugify(instance.name)

        if commit:
            instance.save()
        return instance
