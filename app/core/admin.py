from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    """define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name', 'is_active', 'is_staff', 'user_role']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'image', 'DOB', 'user_role', 'pka', 'ipi_number',
        'pro', 'label_affiliation', 'publisher_affiliation',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'),{'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets= (
        (None, {
            'classes':('wide',),
            'fields':(
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
                'image',
                'DOB',
                'user_role',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.PRO)
admin.site.register(models.labelAffiliation)
admin.site.register(models.publisherAffiliation)
