from django.contrib import admin
from .models import Service


@admin.register(Service)
class PtsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'description', 'publish_date', 'updated_date', 'is_published']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['-price', 'title']
    # actions = ['set_to_published', 'set_to_draft']
    search_fields = ['is_published', 'title']
    # list_filter = [PassportFilter, 'is_published', 'category__name']
    # readonly_fields = ['post_photo']
