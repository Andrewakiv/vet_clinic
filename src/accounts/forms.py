from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

from accounts.models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

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

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = get_user_model().objects.exclude(id=self.instance.id) \
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

