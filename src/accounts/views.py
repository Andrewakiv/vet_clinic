from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class MyCustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'contacts-form__input-name'


class LoginUser(LoginView):
    form_class = MyCustomLoginForm
    template_name = 'accounts/login.html'


class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
    extra_context = {'title': 'Logout'}