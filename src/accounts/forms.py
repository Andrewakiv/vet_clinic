from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ClearableFileInput

from accounts.models import Profile, StaffProfile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control'}),
            # 'password': forms.TextInput(
            #     attrs={'class': 'form-control', "id":"floatingPassword"}),
            # 'password2': forms.PasswordInput(
            #     attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            # 'name': forms.TextInput(
            #     attrs={'class': 'contacts-form__input-name', 'placeholder': 'Enter your full name'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = get_user_model().objects.exclude(id=self.instance.id) \
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'vet_clinic/widgets/custom_clearable_file_input.html'


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'class': 'contacts-form__input-service',
                                                                          'type': 'date'}))

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo', 'send_mail']
        widgets = {
            'photo': CustomClearableFileInput(
                attrs={'class': 'form-control'}),
        }


class StaffProfileEditForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['position', 'description']
        widgets = {
            'position': forms.TextInput(
                attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control'})
        }
