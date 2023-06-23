from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import EngineerTB


class UserAdmin(BaseUserAdmin):
    list_display = ("usr_id", "uid", "name", "phonenum", "is_staff",)
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {'fields': ('usr_id', 'password')}),
        ('Personal Info', {'fields': ('uid', 'name', 'phonenum',)}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usr_id', 'uid', 'name', 'phonenum', 'password'),
            },
        ),
    )
    
    search_fields = ('usr_id',)
    ordering = ('usr_id',)
    filter_horizontal = ()
    
admin.site.register(EngineerTB, UserAdmin)
admin.site.unregister(Group)