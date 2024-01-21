from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'send_mail']
    raw_id_fields = ["user"]
