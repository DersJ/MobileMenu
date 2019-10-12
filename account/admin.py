from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import ugettext_lazy as _

from account import models


# Create your models here.
@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    date_hierarchy = 'time_created'
    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        (_('Personal Information'), {
            'fields': ('name', 'email', 'phone'),
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Time Information'), {
            'fields': ('time_created', 'time_updated'),
        }),
    )
    list_display = (
        'username',
        'name',
        'is_active',
        'is_staff',
        'is_superuser',
        'time_created',
    )
    ordering = None
    readonly_fields = ('time_created', 'time_updated')
    search_fields = ('name', 'username')

