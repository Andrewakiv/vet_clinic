from django.contrib import admin
from .models import Service, Team, Post, Category, Testimonial, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'description', 'publish_date', 'updated_date', 'is_published']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['-price', 'title']
    # actions = ['set_to_published', 'set_to_draft']
    search_fields = ['is_published', 'title']
    # list_filter = [PassportFilter, 'is_published', 'category__name']
    # readonly_fields = ['post_photo']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position', 'description', 'photo', 'publish_date', 'updated_date', 'is_published']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}
    ordering = ['-publish_date', 'name']
    search_fields = ['is_published', 'name']


@admin.register(Post)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'description', 'publish_date', 'updated_date', 'is_published']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['-publish_date', 'title']
    search_fields = ['publish_date', 'title']


@admin.register(Category)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name']


@admin.register(Testimonial)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'response', 'publish_date', 'is_published']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}
    ordering = ['-publish_date', 'name']
    search_fields = ['publish_date', 'name']


@admin.register(Order)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'pet_info', 'service', 'order_date', 'date_for_visit']
    list_display_links = ['id', 'name']
    ordering = ['-order_date', 'name']
    search_fields = ['name', 'pet_info']
