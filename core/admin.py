"""
Django admin configuration for the core app.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _ # for translating fieldset titles in the admin interface

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id'] # Order users by their ID
    list_display = ['email', 'name'] # Display email and name in the user list
    fieldsets = ( # Define the fields to display on the user edit page
        (None, {'fields': ('email', 'password')}), # Basic info section with email and password
        (
            _('Permissions'), # Permissions section with is_active, is_staff, and is_superuser
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}), # Important dates section with last login
    )
    readonly_fields = ['last_login'] # Make last_login a read-only field
    add_fieldsets = ( # Define the fields to display on the user creation page
        (None, {
            'classes': ('wide',), # Use wide layout for the add user form
            'fields': (
                'email', 
                'password1', 
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ) # Fields for creating a new user
        }),
    )


admin.site.register(models.User, UserAdmin) # Register the User model with the custom UserAdmin