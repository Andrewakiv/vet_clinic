from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('posts/<slug:blog_slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('posts/category/<slug:category_blog_slug>/', views.CategoryBlogView.as_view(), name='category_blog'),
    path('like/', views.post_like, name='post_like'),
]
