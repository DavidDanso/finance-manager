from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Profile

class UserAdmin(BaseUserAdmin):
    # Define the fields to be used in displaying the User model.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Role'), {'fields': ('role',)}),  # Add the custom 'role' field here
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'username', 'email', 'updated_time_stamp', 'created_time_stamp')
    search_fields = ('user__username', 'name', 'username', 'email')
    readonly_fields = ('id', 'created_time_stamp', 'updated_time_stamp')

# Register the custom User model and the Profile model
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
