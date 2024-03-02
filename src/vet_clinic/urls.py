from django.urls import path
from . import views

app_name = 'vet_clinic'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('services/<slug:service_slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('faq/', views.faq, name='faq'),
    path('responses/', views.responses, name='responses'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<slug:service_slug>/', views.contacts, name='contacts_detail'),
]
