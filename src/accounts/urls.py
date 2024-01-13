from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),

    path('register/', views.register, name='register'),

    path('password-change/', views.UserChangePassword.as_view(), name='password_change'),
    path('password-change_done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),

]
