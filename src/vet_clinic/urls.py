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
    path('orders/draft/', views.draft_orders, name='draft_orders'),
    path('orders/completed/', views.completed_orders, name='completed_orders'),
    path('orders/confirmed/', views.confirmed_orders, name='confirmed_orders'),
    path('orders/postponed/', views.delayed_orders, name='delayed_orders'),
    path('orders/', views.show_orders, name='show_orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/complete/', views.complete_order, name='complete_order'),
    path('orders/<int:order_id>/confirm/', views.confirm_order, name='confirm_order'),
    path('orders/<int:order_id>/delay/', views.delay_order, name='delay_order'),
    path('orders/<slug:service_slug>/', views.show_filter_orders, name='show_filter_orders'),
    path('user-orders/<str:user_username>/', views.show_user_orders, name='show_user_orders'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<slug:service_slug>/', views.contacts, name='contacts_detail'),
]
