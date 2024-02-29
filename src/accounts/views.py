import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from accounts.forms import UserRegistrationForm, UserChangePasswordForm, UserEditForm, ProfileEditForm, \
    StaffProfileEditForm
from accounts.models import Profile, StaffProfile
from actions.models import Actions
from actions.utils import create_action

logger = logging.getLogger('accounts')


class MyCustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'contacts-form__input-name'


class LoginUser(LoginView):
    form_class = MyCustomLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        logger.info(f'User {username} has logged in')
        return super().form_valid(form)


class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
    extra_context = {'title': 'Logout'}

    def dispatch(self, request, *args, **kwargs):
        username = request.user.username
        logger.info(f'User {username} has logged out.')
        return super().dispatch(request, *args, **kwargs)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            StaffProfile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            logger.info(f'User {form.cleaned_data["username"]} has registered.')
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


class UserChangePassword(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')

    def dispatch(self, request, *args, **kwargs):
        username = request.user.username
        logger.info(f'User {username} has changed password.')
        return super().dispatch(request, *args, **kwargs)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        staff_profile_form = None
        if request.user.groups.filter(name='moderator').exists():
            staff_profile_form = StaffProfileEditForm(instance=request.user.staffprofile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        if staff_profile_form and staff_profile_form.is_valid():
            staff_profile_form.save()
        logger.info(f'User {request.user.username} has edited profile.')
        return redirect('accounts:edit')
            # messages.success(request, 'Profile updated successfully')
        # else:
        # messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        staff_profile_form = None
        if request.user.groups.filter(name='moderator').exists():
            staff_profile_form = StaffProfileEditForm(instance=request.user.staffprofile)

    data = {
        'user_form': user_form,
        'profile_form': profile_form,
        'staff_profile_form': staff_profile_form
    }

    return render(request, 'accounts/edit.html', context=data)


def profile_to_view(request, user_username):
    user_to_view = get_object_or_404(User, username=user_username)
    actions = Actions.objects.filter(user=request.user)

    data = {
        'user_to_view': user_to_view,
        'actions': actions
    }

    return render(request, 'accounts/profile.html', context=data)


