from django.urls import path
from . import views

app_name = 'vet_clinic'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('responses/', views.responses, name='responses'),
    path('contacts/', views.contacts, name='contacts'),
]
