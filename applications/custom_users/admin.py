from django.contrib import admin

from applications.custom_users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'created_at', 'updated_at', 'is_active']