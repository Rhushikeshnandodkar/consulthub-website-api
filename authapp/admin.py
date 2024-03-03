from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login', 'phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_consultent', 'is_influhencer')
    fieldsets = (
        ('User Information', {'fields': ('phone_number', 'username', 'email', 'password', 'is_consultent', 'is_influhencer', 'first_name', 'last_name', 'interests')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
        ('Otp', {'fields': ('otp', 'is_profile_completed')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email')  

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(InterestModel)