from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from accounts.forms import UserRegistrationForm, UserChangePasswordForm, UserEditForm, ProfileEditForm, \
    StaffProfileEditForm
from accounts.models import Profile
from vet_clinic.models import Order


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


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


class UserChangePassword(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')


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
        if staff_profile_form.is_valid():
            if staff_profile_form:
                staff_profile_form.save()
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
    print(request.user.groups.filter(name='moderator').exists())
    data = {
        'user_to_view': user_to_view,
    }

    return render(request, 'accounts/profile.html', context=data)


