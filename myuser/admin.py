from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ['username', 'id', 'email', 'uuid', 'node42_auth_level',
                    'email_verification', 'admin_verification']  # 添加node42_auth_level到展示字段
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'avatar', 'uuid', 'node42_auth_level',
         'email_verification', 'admin_verification')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'avatar', 'node42_auth_level',
         'email_verification', 'admin_verification')}),
    )
    readonly_fields = ('uuid', 'date_joined', 'last_login')  # 将uuid字段设为只读


admin.site.register(models.CustomUser, CustomUserAdmin)
