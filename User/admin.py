from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Customers


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'phone', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('email',)
    search_fields = ('email', 'name', 'phone')
    readonly_fields = ('date_joined', 'last_login','created_at','updated_at',)

    ordering = ('email',)

  
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined','created_at','updated_at',)}),
        
        

    )

   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Customers)