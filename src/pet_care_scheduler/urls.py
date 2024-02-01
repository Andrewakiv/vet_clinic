from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('orders/draft/', views.draft_orders, name='draft_orders'),
    path('orders/completed/', views.completed_orders, name='completed_orders'),
    path('orders/confirmed/', views.confirmed_orders, name='confirmed_orders'),
    path('orders/postponed/', views.delayed_orders, name='delayed_orders'),
    path('orders/', views.show_orders, name='show_orders'),
    path('user-orders/<str:user_username>/', views.show_user_orders, name='show_user_orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/complete/', views.complete_order, name='complete_order'),
    path('orders/<int:order_id>/confirm/', views.confirm_order, name='confirm_order'),
    path('orders/<int:order_id>/delay/', views.delay_order, name='delay_order'),
    path('orders/<slug:service_slug>/', views.show_filter_orders, name='show_filter_orders'),
]
