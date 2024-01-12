from django.urls import path
from . import views

app_name = 'vet_clinic'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:service_slug>/', views.service_detail, name='service_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<slug:category_blog_slug>/', views.category_blog, name='category_blog'),
    path('faq/', views.faq, name='faq'),
    path('responses/', views.responses, name='responses'),
    path('contacts/', views.contacts, name='contacts'),
]
