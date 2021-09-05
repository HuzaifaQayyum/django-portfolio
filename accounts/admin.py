from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User

class UserAdmin(BaseUserAdmin):
    ordering        = ['email']
    list_display    = ['name', 'email']
    list_display_links = ['name', 'email']
    fieldsets = [
        (_('Security'), { 'fields': ['email', 'password' ]}),
        (_('Personal Info'), { 'fields': ['name'] }),
        (_('Permissions'), { 'fields': ['is_active', 'is_staff', 'is_superuser']}),
        (_('Important Dates'), { 'fields': ['last_login'] })
    ]
    add_fieldsets = [
        (_('Security'), { 'fields': ['email', 'password' ]}),
        (_('Personal Info'), { 'fields': ['name'] }),
        (_('Permissions'), { 'fields': ['is_active', 'is_staff', 'is_superuser']})
    ]


admin.site.register(User, UserAdmin)