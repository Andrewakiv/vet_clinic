from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'description', 'publish_date', 'updated_date', 'is_published']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['-publish_date', 'title']
    search_fields = ['publish_date', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name']
