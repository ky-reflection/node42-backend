from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'uuid', 'role']  # 添加role到展示字段
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'avatar', 'uuid', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'avatar', 'role')}),
    )
    readonly_fields = ('uuid',)  # 将uuid字段设为只读

admin.site.register(CustomUser, CustomUserAdmin)
