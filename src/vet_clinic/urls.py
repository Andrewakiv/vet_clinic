from django.urls import path
from . import views

app_name = 'vet_clinic'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('services/<slug:service_slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:blog_slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/category/<slug:category_blog_slug>/', views.CategoryBlogView.as_view(), name='category_blog'),
    path('like/', views.post_like, name='post_like'),
    path('faq/', views.faq, name='faq'),
    path('responses/', views.responses, name='responses'),
    path('orders/', views.show_orders, name='show_orders'),
    path('user-orders/<str:user_username>/', views.show_user_orders, name='show_user_orders'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<slug:service_slug>/', views.contacts, name='contacts_detail'),
]
