from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    # path('orders/confirmed/<slug:service_slug>/', views.confirm_filter_orders, name='confirm_filter_orders'),
    path('orders/draft/', views.DraftOrders.as_view(), name='draft_orders'),
    path('orders/completed/', views.CompletedOrders.as_view(), name='completed_orders'),
    path('orders/confirmed/', views.ConfirmedOrders.as_view(), name='confirmed_orders'),
    path('orders/postponed/', views.DelayedOrders.as_view(), name='delayed_orders'),
    path('orders/', views.ShowOrders.as_view(), name='show_orders'),
    path('user-orders/<str:user_username>/', views.UserOrders.as_view(), name='show_user_orders'),
    path('orders/<int:order_id>/', views.OrderDetail.as_view(), name='order_detail'),
    path('orders/<int:order_id>/complete/', views.CompleteOrder.as_view(), name='complete_order'),
    path('orders/<int:order_id>/confirm/', views.ConfirmOrder.as_view(), name='confirm_order'),
    path('orders/<int:order_id>/delay/', views.DelayOrder.as_view(), name='delay_order'),
    path('orders/<int:order_id>/postpone/', views.PostponeOrder.as_view(), name='postpone_order'),
    path('orders/<slug:service_slug>/', views.FilterOrders.as_view(), name='show_filter_orders'),
]
